import socket

def Main():
        host= '172.32.247.1'
        port = 5001

        server = ('172.32.247.2', 5000)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host,port))

        message = input("->")
        while message != 'q':
                sock.sendto(message.encode('utf-8'), server)
                data, addr = sock.recvfrom(1024)
                data = data.decode('utf-8')
                print("Recieved from server: "+ data)
                message = input("->")
        sock.close()

if __name__ == '__main__':
        Main()