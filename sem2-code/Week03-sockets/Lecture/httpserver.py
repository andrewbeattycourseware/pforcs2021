#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8081  # Port to listen on (non-privileged ports are > 1023)

def proccess_header(rawHeader):
    lines = rawHeader.split('\r\n')
    print (' we got ', lines , 'in the header')
    header = {}
    # process the request line we should have some error checking here
    requestEntities = lines[0].split(' ')
    header['method'] = requestEntities[0].strip()
    header['resource'] = requestEntities[1].strip()
    header['protocol'] = requestEntities[2].strip()
    # we should process the header attributes here 
    return header

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        readingheader = True
        readbuffer = b""
        while readingheader:
            readbuffer += conn.recv(4098)
            read_string = readbuffer.decode()
            endHeader = read_string.find('\r\n\r\n')  # an empty line
            headerString = read_string[:endHeader]
            readbuffer = readbuffer[endHeader+4:] # the body if there is one
            header = proccess_header(headerString)
            readingheader = False
            print (repr(header))
            
        responseString = '' + header['protocol'] + ' 200 OK\r\n\r\na page\n'
        
        conn.sendall(responseString.encode()) # ok this should be doing a bit more see app-server
        
