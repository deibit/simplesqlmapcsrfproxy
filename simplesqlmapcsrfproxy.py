import requests
import sys

from importlib import import_module
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv) < 4:
    print("Usage simplesqlmapcsrfproxy.py <url> <cookie=value> <my_processor.py>")
    sys.exit()

URL = sys.argv[1]
COOKIE = dict([tuple(sys.argv[2].split('='))])
PROCESSOR = import_module(sys.argv[3])
PORT = 54321

def req():
    res = requests.get(URL, cookies=COOKIE)
    if res.status_code == 200:
        return PROCESSOR.process(res.text)
    print(f"[!] Error requesting page: {URL}")

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        content = req().encode("utf-8")
        self.wfile.write(content)

def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=PORT):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"[+] Starting web server at {PORT}")
    print(f"[+] Using cookie: {COOKIE}")
    print(f"[+] Using url   : {URL}")

    httpd.serve_forever()

if __name__ == '__main__':
    run()
