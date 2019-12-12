from socket import *
import sys

def portscanner(ip,port):
    s = socket(AF_INET,SOCK_STREAM)
    try:
        s.settimeout(8)
        result = s.connect_ex((ip,port))
        if result == 0:
            sys.stdout.write("%s:%d \n" % (ip, port))
    except:
        add_file.close()
        s.close()
    s.close()