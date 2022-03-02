import socket
HOST = '192.168.0.107'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

msg = raw_input()
udp.sendto (msg, dest)
n = udp.recv(1024)
print n
udp.close()
