n = int(input("Digite um número inteiro: "))
        
def fatorial(n):
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
    print(f)

while n >= 0:
    fatorial(n)
    n = int(input("Digite um número inteiro: "))
