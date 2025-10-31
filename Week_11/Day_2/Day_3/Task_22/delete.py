from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data=[]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())
    def do_DELETE(self):
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)
        delete_data = json.loads(parsed_data)
        delete_name = delete_data.get("name")
        for entry in data:
            if entry.get("name") == delete_name:
                data.remove(entry)
                break
        self.send_data([
            {"message": "Data deleted successfully"},
            {"deleted_data": delete_data}
        ], status=404)
def run():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, BasicAPI)
    print('Starting server on port 5000...')
    httpd.serve_forever()
print("Delete message abeg!")
run()