# Asciiverse: installs av, the terminal client, for the current user.
#
#   irm https://asciiverse.sh/install.ps1 | iex
#
# Downloads the av archive for this machine, checks it against SHA256SUMS,
# puts av.exe in %LOCALAPPDATA%\Asciiverse\bin and adds that folder to your
# user PATH. No administrator rights needed.
#
# Settings, all optional:
#   $env:AV_INSTALL_DIR   where av.exe goes
#   $env:AV_DOWNLOAD_URL  folder holding the archives and SHA256SUMS
#                         (default https://asciiverse.sh/releases/av/latest)

& {
  $ErrorActionPreference = 'Stop'
  $ProgressPreference = 'SilentlyContinue'   # the progress bar makes Invoke-WebRequest very slow
  [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

  # The download bar: green blocks on a faint track, then percent, size,
  # speed and time left. Built here rather than with Invoke-WebRequest's own,
  # which is the slow one. Block characters come from their code points, so
  # the script itself stays ASCII.
  function Format-Size([double]$n) {
    if ($n -lt 1e3) { return '{0:0} B' -f $n }
    if ($n -lt 1e6) { return '{0:0} kB' -f ($n / 1e3) }
    if ($n -lt 1e9) { return '{0:0.0} MB' -f ($n / 1e6) }
    return '{0:0.00} GB' -f ($n / 1e9)
  }
  function Write-Bar([long]$done, [long]$total, [double]$secs) {
    $w = 30
    $rate = ''
    if ($secs -ge 0.5) {
      $speed = $done / $secs
      $rate = '  ' + (Format-Size $speed) + '/s'
      if ($total -gt $done -and $speed -gt 0) {
        $left = [math]::Ceiling(($total - $done) / $speed)
        $rate += if ($left -lt 60) { "  $left s left" } else { '  ' + [math]::Floor($left / 60) + ' min left' }
      }
    }
    [Console]::Write("`r  ")
    if ($total -gt 0) {
      $full = [math]::Floor([math]::Min($done, $total) * $w / $total)
      Write-Host -NoNewline ([string][char]0x2588 * $full) -ForegroundColor Green
      Write-Host -NoNewline ([string][char]0x2500 * ($w - $full)) -ForegroundColor DarkGray
      $info = ' {0,3}%  {1} / {2}{3}' -f [math]::Floor($done * 100 / $total), (Format-Size $done), (Format-Size $total), $rate
    } else {
      $info = (Format-Size $done) + $rate
    }
    # pad over whatever a longer previous line left behind
    Write-Host -NoNewline ($info.PadRight(48)) -ForegroundColor Yellow
  }
  function Get-WithBar([string]$Url, [string]$OutFile) {
    if ([Console]::IsOutputRedirected) {
      Invoke-WebRequest -UseBasicParsing $Url -OutFile $OutFile
      return
    }
    Add-Type -AssemblyName System.Net.Http
    $client = New-Object System.Net.Http.HttpClient
    $file = $null
    try {
      $resp = $client.GetAsync($Url, [System.Net.Http.HttpCompletionOption]::ResponseHeadersRead).GetAwaiter().GetResult()
      [void]$resp.EnsureSuccessStatusCode()
      $total = [long]0
      if ($resp.Content.Headers.ContentLength) { $total = [long]$resp.Content.Headers.ContentLength }
      $in = $resp.Content.ReadAsStreamAsync().GetAwaiter().GetResult()
      $file = [IO.File]::Create($OutFile)
      $buf = New-Object byte[] 65536
      $done = [long]0
      $clock = [Diagnostics.Stopwatch]::StartNew()
      $drawn = [long]-1000
      while (($n = $in.Read($buf, 0, $buf.Length)) -gt 0) {
        $file.Write($buf, 0, $n)
        $done += $n
        if ($clock.ElapsedMilliseconds - $drawn -ge 66) {
          Write-Bar $done $total $clock.Elapsed.TotalSeconds
          $drawn = $clock.ElapsedMilliseconds
        }
      }
      Write-Bar $done $total $clock.Elapsed.TotalSeconds
      Write-Host ''
    } finally {
      if ($file) { $file.Dispose() }
      $client.Dispose()
    }
  }

  $DownloadUrl = if ($env:AV_DOWNLOAD_URL) { $env:AV_DOWNLOAD_URL } else { 'https://asciiverse.sh/releases/av/latest' }
  $InstallDir = if ($env:AV_INSTALL_DIR) { $env:AV_INSTALL_DIR } else { Join-Path $env:LOCALAPPDATA 'Asciiverse\bin' }

  # Kept to plain ASCII: irm decodes by the server's charset, and a guess
  # there would turn block letters into mojibake.
  Write-Host '  ASCIIVERSE' -ForegroundColor Green
  Write-Host '  Where text comes alive' -ForegroundColor Yellow
  Write-Host ''

  $arch = $env:PROCESSOR_ARCHITEW6432
  if (-not $arch) { $arch = $env:PROCESSOR_ARCHITECTURE }
  switch ($arch) {
    'AMD64' { $target = 'x86_64-pc-windows-msvc' }
    'ARM64' { $target = 'aarch64-pc-windows-msvc' }
    default { throw "no av build for the $arch processor yet" }
  }
  $archive = "av-$target.zip"

  $tmp = Join-Path ([IO.Path]::GetTempPath()) ("av-install-" + [Guid]::NewGuid())
  New-Item -ItemType Directory -Path $tmp | Out-Null
  try {
    Write-Host "  fetching av ($target)" -ForegroundColor DarkGray
    Invoke-WebRequest -UseBasicParsing "$DownloadUrl/SHA256SUMS" -OutFile "$tmp\SHA256SUMS"
    Get-WithBar "$DownloadUrl/$archive" "$tmp\$archive"

    $want = $null
    foreach ($line in Get-Content "$tmp\SHA256SUMS") {
      $parts = $line -split '\s+', 2
      if ($parts.Count -eq 2 -and $parts[1].TrimStart('*') -eq $archive) { $want = $parts[0].ToLower() }
    }
    if (-not $want) { throw "SHA256SUMS has no line for $archive" }
    $got = (Get-FileHash -Algorithm SHA256 "$tmp\$archive").Hash.ToLower()
    if ($want -ne $got) { throw "checksum mismatch for $archive (expected $want, got $got); nothing installed" }
    Write-Host '  sha256 ok' -ForegroundColor DarkGray

    Expand-Archive -Path "$tmp\$archive" -DestinationPath "$tmp\x" -Force
    if (-not (Test-Path "$tmp\x\av.exe")) { throw "$archive does not contain av.exe" }

    New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
    Copy-Item -Force "$tmp\x\av.exe" (Join-Path $InstallDir 'av.exe')
    Write-Host "  installed to $InstallDir\av.exe" -ForegroundColor DarkGray
  } finally {
    Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
  }

  # Windows has no shell rc file to edit by hand, so add the folder to the
  # user PATH the way rustup and scoop do. Removing it is one edit in
  # "Edit environment variables for your account".
  $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
  $entries = @($userPath -split ';' | Where-Object { $_ })
  if ($entries -notcontains $InstallDir) {
    [Environment]::SetEnvironmentVariable('Path', (($entries + $InstallDir) -join ';'), 'User')
    Write-Host "  added $InstallDir to your user PATH" -ForegroundColor DarkGray
  }
  if (($env:Path -split ';') -notcontains $InstallDir) { $env:Path = "$env:Path;$InstallDir" }

  Write-Host ''
  Write-Host '  Done. Type av to open the catalog (open a new terminal if it is not found).'
}
