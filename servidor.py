import socket as so

host = ''
porta = 50000
servidor = (host, porta)

udp = so.socket(so.AF_INET, so.SOCK_DGRAM)

udp.bind(servidor)

print(f'O servidor {udp.getsockname()} está online!!')

while True:
  dados, cliente = udp.recvfrom(255)
  mensagem = dados.decode('utf-8')


  print(f'o cliente {cliente} disse: ', mensagem)

  cont_dados = len(mensagem)
  mensagem_conf = (f' A conexão com o servidor {udp.getsockname()} foi bem sucedido')
  dados2 = mensagem_conf.encode('utf-8')
  udp.sendto(dados2, cliente)
