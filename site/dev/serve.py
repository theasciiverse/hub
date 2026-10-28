#!/usr/bin/env python3
"""The local dev server: python's http.server, but every response says
Cache-Control: no-cache, so the browser checks for a newer file on each load
instead of showing a stale catalog or page. Run from the site folder:
    python3 dev/serve.py            # http://127.0.0.1:8765/"""
import functools, http.server, os, sys

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
http.server.ThreadingHTTPServer(("127.0.0.1", port), functools.partial(NoCache, directory=root)).serve_forever()
