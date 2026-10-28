#!/usr/bin/env python3
"""Show a MUD's greeting screen: connect, refuse every telnet option, print
what the server sends for a few seconds, then hang up. Recorded under
asciinema (dev/record_muds.sh) it gives each MUD its preview and front picture
without logging in. Usage: mud_greet.py host port [tls|plain] [seconds] [encoding]
encoding: the server's character set, e.g. cp437 for DOS ANSI art (default utf-8, passed through)"""
import socket, ssl, sys, time

IAC, DONT, DO, WONT, WILL, SB, SE = 255, 254, 253, 252, 251, 250, 240

def main():
    host, port = sys.argv[1], int(sys.argv[2])
    tls = len(sys.argv) > 3 and sys.argv[3] == "tls"
    secs = float(sys.argv[4]) if len(sys.argv) > 4 else 12
    enc = sys.argv[5] if len(sys.argv) > 5 else None
    s = socket.create_connection((host, port), timeout=10)
    if tls:
        s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
    s.settimeout(0.3)
    out = sys.stdout.buffer
    end = time.time() + secs
    buf, state = b"", 0
    while time.time() < end:
        try:
            data = s.recv(65536)
        except (socket.timeout, TimeoutError):
            continue
        if not data:
            break
        clean = bytearray()
        i = 0
        while i < len(data):
            b = data[i]
            if state == 0:
                if b == IAC: state = 1
                else: clean.append(b)
            elif state == 1:
                if b in (DO, DONT, WILL, WONT): state = b
                elif b == SB: state = SB
                elif b == IAC: clean.append(IAC); state = 0
                else: state = 0
            elif state in (DO, DONT, WILL, WONT):
                # refuse everything: no compression, no window size, plain text
                if state == DO: s.sendall(bytes([IAC, WONT, b]))
                elif state == WILL: s.sendall(bytes([IAC, DONT, b]))
                state = 0
            elif state == SB:
                if b == IAC: state = SE
            elif state == SE:
                state = 0 if b == SE else SB
            i += 1
        text = bytes(clean).replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
        if enc:
            text = text.decode(enc, errors="replace").encode("utf-8")
        out.write(text); out.flush()
    s.close()

if __name__ == "__main__":
    main()
