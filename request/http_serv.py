from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        dt = datetime.now().strftime("%H:%M:%S").encode("utf-8")
        self.wfile.write(dt)
        print(dt)

    def do_POST(self):
        print(self.client_address)
        print(self.rfile.readlines(1)[0])
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"hello!")


serv = HTTPServer(("0.0.0.0", 3333), HttpProcessor)
serv.serve_forever()
