from http.server import HTTPServer, SimpleHTTPRequestHandler
server_address = ('', 8080)
myserver = HTTPServer(server_address, SimpleHTTPRequestHandler)
myserver.serve_forever()