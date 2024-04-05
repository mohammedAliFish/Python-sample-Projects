import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('192.168.31.65',5555))

while True:
    Rdata , address = sock.recvfrom(1024)
    data = Rdata.decode('UTF-8')
    print("Requst from {} : \n ".format(address,data))
    print('-----------------------')
    msg = str(input())
    print("------------------------")
    Sdata = msg.encode('UTF-8')
    sock.sendto(Sdata,address)
    print("Server respond !")
