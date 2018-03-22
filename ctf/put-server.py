"""
Description: This script is a simple python web server which accepts a PUT request and writes the supplied data to a file.
There is a known issue with the signal module when trying to run this on Windows 7.  It has worked in various *nix environments.

This script is a combination of the following links:
https://gist.githubusercontent.com/codification/1393204/raw/3fd4a48d072ec8f7f453d146814cb6e7fc6a129f/server.py
http://www.acmesystems.it/python_httpserver
"""
import sys
import signal
from os import curdir, sep
import cgi
from threading import Thread
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class PUTHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        print self.headers
        length = int(self.headers['Content-Length'])
        try:
            with open(curdir + self.path, "wb") as dst:
                dst.write(self.rfile.read(length))

            print 'PUT Succeeded'
            self.send_response(200)
        except Exception as e:
            print 'PUT Failed '
            print e


    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    #Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
            self.path="/index.html"

        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                    mimetype='text/html'
                    sendReply = True
            if self.path.endswith(".jpg"):
                    mimetype='image/jpg'
                    sendReply = True
            if self.path.endswith(".gif"):
                    mimetype='image/gif'
                    sendReply = True
            if self.path.endswith(".js"):
                    mimetype='application/javascript'
                    sendReply = True
            if self.path.endswith(".css"):
                    mimetype='text/css'
                    sendReply = True

            if sendReply == True:
                    #Open the static file requested and send it
                    f = open(curdir + sep + self.path) 
                    self.send_response(200)
                    self.send_header('Content-type',mimetype)
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
            return


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
            
def run_on(port):
    print("Starting a server on port %i" % port)
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, PUTHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print "Usage: put-server.py <port #>"
        sys.exit()
    ports = [int(arg) for arg in sys.argv[1:]]
    for port_number in ports:
        server = Thread(target=run_on, args=[port_number])
        server.daemon = True # Do not make us wait for you to exit
        server.start()
    signal.pause() # Wait for interrupt signal, e.g. KeyboardInterrupt
    
