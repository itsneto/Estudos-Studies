
tamanho = int(input("Digite o tameanho da sequência de números: "))

produto = 1
i = 0

valor = 1

while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("O produto dos valores digitados é:", produto)
