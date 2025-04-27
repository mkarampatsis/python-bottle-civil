from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloWorldHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # Send HTTP status code 200 (OK)
    self.send_response(200)

    # Send headers
    self.send_header('Content-type', 'text/html')
    self.end_headers()

    # Send the response body
    self.wfile.write(b"Hello, World!")

# Server settings
host = "localhost"
port = 8000

# Create and start the server
with HTTPServer((host, port), HelloWorldHandler) as server:
  print(f"Serving on http://{host}:{port}")
  server.serve_forever()

# http://localhost:8000/