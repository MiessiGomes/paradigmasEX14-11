 import socket

def validar_endereco(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Leitura do arquivo de entrada
with open('entrada.txt', 'r') as entrada_arquivo:
    enderecos = entrada_arquivo.read().split()

enderecos_validos = []
enderecos_invalidos = []

for endereco in enderecos:
    if validar_endereco(endereco):
        enderecos_validos.append(endereco)
    else:
        enderecos_invalidos.append(endereco)
        
with open('saida.txt', 'w') as saida_arquivo:
    saida_arquivo.write("[Endereços válidos:] " + ' '.join(enderecos_validos) + "\n")
    saida_arquivo.write("[Endereços inválidos:] " + ' '.join(enderecos_invalidos) + "\n")

print("Processo concluído. Verifique o arquivo 'saida.txt'.")