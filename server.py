from http.server import HTTPServer, BaseHTTPRequestHandler
from load_configrations import Config

#load configration from .env file
try:
    config = Config()
    config.load()
except Exception as msg:
    print("-- {msg}".format(msg=msg))

print(config.get('SERV_ROOT_PATH'))

#create server class
class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(config.get('SERV_ROOT_PATH') + self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


#start server
httpd = HTTPServer((config.get('SERV_NAME'), int(config.get('SERV_PORT'))), Serv)
httpd.serve_forever()