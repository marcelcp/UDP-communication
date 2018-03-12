import socket

def Main():

        sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address=('172.32.247.2',5000)
        sock.bind(address)
        print("Server Started")

        while True:
                data, addr = sock.recvfrom(1024)
                data=data.decode('utf-8')
                print("recieved message: " + str(addr))
                print("From Connected user: " + data)
                data = data.upper()
                print("Sending: "+ data)
                sock.sendto(data.encode('utf-8'),addr)
        c.close()

if __name__ == '__main__':
        Main()