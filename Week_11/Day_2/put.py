from http.server import BaseHTTPRequestHandler, HTTPServer
import json


data=[]


class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())


    def do_PUT(self):
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)
        put_data = json.loads(parsed_data)
        update_name = put_data.get("name")
        for entry in data:
            if entry.get("name") == update_name:
                entry.update(put_data)
                break
        else:
            data.append(put_data)
        self.send_data([
            {"message": "Data updated successfully"},
            {"updated_data": put_data}
        ], status=200)
def run():
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, BasicAPI)
    print('Starting server on port 5000...')
    httpd.serve_forever()
print("The server is running!")
run()











