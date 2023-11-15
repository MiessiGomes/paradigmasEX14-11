def bytes_para_megabytes(bytes):
    return bytes / (1024 * 1024)

def calcular_percentual(total, individual):
    return (individual / total) * 100

with open('usuarios.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

usuarios = []
total_uso = 0

for linha in linhas:
    nome, uso_em_bytes = linha.split()
    uso_em_bytes = int(uso_em_bytes)
    total_uso += uso_em_bytes
    usuarios.append({'nome': nome, 'uso': uso_em_bytes})


total_uso_mb = bytes_para_megabytes(total_uso)
for usuario in usuarios:
    usuario['uso_mb'] = bytes_para_megabytes(usuario['uso'])
    usuario['percentual'] = calcular_percentual(total_uso, usuario['uso'])


usuarios = sorted(usuarios, key=lambda x: x['uso'], reverse=True)

with open('relatorio.txt', 'w') as relatorio:
    relatorio.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 60 + "\n")
    relatorio.write("Nr. Usuário Espaço utilizado % do uso\n")

    for i, usuario in enumerate(usuarios, start=1):
        relatorio.write(f"{i} {usuario['nome']: <10} {usuario['uso_mb']: >12.2f} MB {usuario['percentual']: >8.2f}%\n")

    relatorio.write(f"\nEspaço total ocupado: {total_uso_mb:.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {(total_uso_mb / len(usuarios)):.2f} MB\n")

print("Relatório gerado com sucesso no arquivo 'relatorio.txt'.")