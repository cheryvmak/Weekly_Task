from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "name":"yemi",
        "track":"AI Engr"
    }
]


class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 201):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_PATCH(self):
        content_size = int(self.headers.get('Content-Length',0))
        parsed_data = self.rfile.read(content_size)

        patch_data = json.loads(parsed_data)
        if data:
            data[0].update(patch_data)
            self.send_data({   
                "message":"Data Edited",
                "data":data[0]
            }, status=201)
        else:
            self.send_data({
                "message":"No data to patch"
            }, status=400)


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
        HTTPServer(('0.0.0.0', 5000), BasicAPI).serve_forever()
print("Application is running!")
run()