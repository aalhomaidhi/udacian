#!/usr/bin/env python3
#
# An HTTP server for Udacians

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class Udacian:
  def __init__(self, name, city, enrollment, nanodegree, status):
    self.name = name
    self.city = city
    # day of the week, am or pm, session lead name 
    self.enrollment = enrollment
    self.nanodegree = nanodegree
    # ontrack, behind or critical 
    self.status = status

  def print_udacian(self):
    return '%s is enrolled in %s studying %s in %s %s with Ms. %s , he/she is %s' % (self.name, self.city, self.nanodegree, self.enrollment[0],
                                                                              self.enrollment[1], self.enrollment[2], self.status)
memory = []

form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="name" placeholder="Name"></textarea>
    <br>
    <textarea name="city" placeholder="City"></textarea>
    <br>
    <textarea name="enrollment" placeholder="Enrollment"></textarea>
    <br>
    <textarea name="nanodegree" placeholder="Nanodegree"></textarea>
    <br>
    <textarea name="status" placeholder="Status"></textarea>
    <br>
    <button type="submit">Press me!</button>
  </form>
  <pre>
{}
  </pre>
'''

class UdacianHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # How long was the data?
        length = int(self.headers.get('Content-length', 0))

        # Read the data
        data = self.rfile.read(length).decode()

        # Parse the data, extracting all form fields 
        name = parse_qs(data)["name"][0]
        city = parse_qs(data)["city"][0]
        enrollment = parse_qs(data)["enrollment"][0]
        nanodegree = parse_qs(data)["nanodegree"][0]
        status = parse_qs(data)["status"][0]



        # Create Udacian object
        udacian = Udacian(name, city, enrollment, nanodegree, status)


        # Store Udacian object in memory
        memory.append(udacian.print_udacian())

        # Send a 303 back to the root page
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        # First, send a 200 OK response
        self.send_response(200)

        # Then send headers
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the form with Udacians objects in it
        mesg = form.format("\n".join(memory))
        self.wfile.write(mesg.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, UdacianHandler)
    httpd.serve_forever()