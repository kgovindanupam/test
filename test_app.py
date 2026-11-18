from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
            <body>
                <h1>Welcome !!!</h1>
            </body>
        </html>
        """

        self.wfile.write(html.encode())

server = HTTPServer(("127.0.0.1", 8000), MyHandler)

print("Application running at http://localhost:8000")

server.serve_forever()