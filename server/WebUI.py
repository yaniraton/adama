import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class WebUI:
    def __init__(self, host='localhost', port=8000):
        self.host = host
        self.port = port
        self.server = None
        self.data = dict()

        # Start the server in a separate thread
        server_thread = threading.Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()

    def start_server(self):
        server_address = (self.host, self.port)
        self.server = HTTPServer(server_address, WebUIHandler)
        print('listening on port', self.port)
        self.server.serve_forever()

    def update_data(self, new_data):
        self.data = new_data

class WebUIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Generate the HTML response with the data
            html = "<html><body>"
            for key, value in self.data.items():
                html += f"<p>{key}: {value}</p>"
            html += "</body></html>"
            self.wfile.write(html.encode())
        else:
            self.send_error(404)
