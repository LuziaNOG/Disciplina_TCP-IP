import socket
HOST = '192.168.0.107'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
	msg, cliente = udp.recvfrom(1024)
	vogais = 0
	for caracter in msg:
		if caracter in 'aeiouAEIOU':
			vogais = vogais + 1
	udp.sendto(str(vogais), cliente)
udp.close()
