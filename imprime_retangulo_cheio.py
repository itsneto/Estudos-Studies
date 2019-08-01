w = int(input("Digite a largura: "))
h = int(input("Digite a altura: "))

def largura(w):
    n = 1
    while n <= w:
        print("#", end="")
        n = n + 1

def altura(h):
    f = 1
    while f <= h:
        largura(w)
        print()
        f = f + 1

if w > 0 and h > 0:
    altura(h)
