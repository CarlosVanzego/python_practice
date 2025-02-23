# Importing the  modules to create an HTTP server
from http.server import HTTPServer, BaseHTTPRequestHandler

# Define a handler class to processs HTTP request 
class helloHandler(BaseHTTPRequestHandler):
  # Method to handle GET requests (request to retrieve data)
  def do_GET(self):
    # Send a 200 OK HTTP status code in the response 
      self.send_response(200)
    # Specify the content type of the response as HTML
      self.send_header('content_type', 'text/html')
    # End the headers section of the HTTP response. 
      self.end_headers()
      self.wfile.write('Hello Carlos'. encode())



def main():
    PORT = 8000
    server = HTTPServer(('', PORT), helloHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()