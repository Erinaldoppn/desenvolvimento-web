import socket as so

HOST = '127.0.0.1'  #Endereço IP do Servidor
PORTA = 50000   # Porta aberta pelo servidor

servidor = (HOST, PORTA) # tupla
udp = so.socket(so.AF_INET, so.SOCK_DGRAM)

print(f'Cliente conectado em ', udp.getsockname())

while True:
    msg = input('Digite a mensagem: ')
    msg_byte = msg.encode('utf-8')      # Mensagem codificada
    udp.sendto(msg_byte, servidor)   # Mensagem enviada

    dados, cliente = udp.recvfrom(255)
    mensagem = dados.decode('utf-8')

    dados, cliente =  udp.recvfrom(255)
    print('Hora do servidor: ', dados.decode('utf-8'))

    msg = 'Erinaldo disse: Hora recebida'+dados.decode('utf-8')
    udp.sendto(msg.encode('utf-8'), servidor )

udp.close()
