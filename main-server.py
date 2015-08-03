'''
ULIMA - Programacion Internet
Servidor que reponde texto
'''

__author__ = "Hernan Quintana"
__copyright__ = "Copyright 2015, ULIMA-PI"
__credits__ = ["Hernan Quintana", "https://wiki.python.org/moin/BaseHttpServer"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Hernan Quintana"
__email__ = "hquintan@ulima.edu.pe"
__status__ = "Production"

import time
import BaseHTTPServer

HOST_NAME = 'localhost'
PORT_NUMBER = 80

class MyServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/text")
        s.end_headers()
        print s.path
        if s.path == "url1":
            s.wfile.write("<html><head><title>Demo 1 - Programacion Internet</title></head>")
            s.wfile.write("<body><p>Esto es una prueba</p></body>")
        elif s.path == "url2":
            s.wfile.write("<html><head><title>Demo 1 - Programacion Internet</title></head>")
            s.wfile.write("<body>")
            s.wfile.write("<h1>Titulo</h1>")
            s.wfile.write("<p>Este un parrafo</p>")
            s.wfile.write("<div>Esta es un div (cuadro)</div>")
            s.wfile.write("</body>")
        elif s.path == "url":
            s.wfile.write("Hola mundo!!")
        else:
            s.send_error(404, "Recurso no encontrado")
            return




if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyServerHandler)
    print time.asctime(), "Server iniciando - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server parado - %s:%s" % (HOST_NAME, PORT_NUMBER)
