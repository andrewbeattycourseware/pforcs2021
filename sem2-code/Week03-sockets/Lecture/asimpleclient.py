# An example script to connect to Google using socket
# programming in Python
import socket  # for socket
import sys
host = 'andrewbeatty1.pythonanywhere.com'
resource = '/books'
method = 'GET'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

#http port
port = 80
try:
    host_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))
print("connected")

httprequest = method + ' ' + resource + ' HTTP/1.1 \r\nHost:'+host+'\r\n\r\n'
s.send(httprequest.encode()) 

# receive data from the server and decoding to get the string.
buffer = s.recv(1024).decode()
httpresponse = repr(buffer)
# we will not get to this line
print("we got " + httpresponse)
s.close()
