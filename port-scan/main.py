import socket

hostname = "www.google.com"

common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 8080]

check_ports = [9999] # as portas que queres checar

def verifyPort(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        code = s.connect_ex((hostname, port))
        if code == 0:
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))
    except:
        pass

for port in common_ports: verifyPort(port)

for port in check_ports: verifyPort(port)