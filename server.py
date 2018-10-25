from http.server import HTTPServer, BaseHTTPRequestHandler
from configrations import Config

#create server class
class SHServer(BaseHTTPRequestHandler):
    global config
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            fileToOpen = open(config.get('SERV_ROOT_PATH') + self.path[1:]).read()
            self.send_response(200)
        except:
            fileToOpen = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(fileToOpen, 'utf-8'))


try:
    #load configration from .env file
    config = Config()
    config.load()

    print(config.get('SERV_ROOT_PATH'))

    httpd = HTTPServer((config.get('SERV_NAME'), int(config.get('SERV_PORT'))), SHServer)
    httpd.serve_forever()

except Exception as msg:
    print("-- {msg}".format(msg=msg))