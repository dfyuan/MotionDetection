import sys
import cv2
import time
import StringIO

from PIL import Image
from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class CamHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
        while True:
            try:
                (read, image) = streamCamera.read()
                if not read:
                    continue
                rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
                jpg = Image.fromarray(rgb)
                jpg_file = StringIO.StringIO()
                jpg.save(jpg_file,'JPEG')
                self.wfile.write("--jpgboundary")
                self.send_header('Content-type','image/jpeg')
                self.send_header('Content-length',str(jpg_file.len))
                self.end_headers()
                jpg.save(self.wfile,'JPEG')
                time.sleep(0.05)
            except KeyboardInterrupt:
                break
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class Stream(object):
    def __init__(self):
        global image
        global streamCamera
        streamCamera = cv2.VideoCapture(0)
        streamCamera.set(3,320)
        streamCamera.set(4,320)

    def stream_main(self):
        try:
            server = ThreadedHTTPServer(('0.0.0.0', 5000), CamHandler)
            print("Streaming HTTPServer started")
            server.serve_forever()
        except KeyboardInterrupt:
            streamCamera.release()
            server.socket.close()
        except Exception as eThreadedHTTPServer:
            pass

if __name__ == '__main__':
    Stream().stream_main()
