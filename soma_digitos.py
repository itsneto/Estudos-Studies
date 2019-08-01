n = int(input("Digite um número inteiro: "))

i = 0

while n > 0:
    c = n % 10
    n = (n - c) // 10
    i = i + c
print(i)
