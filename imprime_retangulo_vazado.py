w = int(input("Digite a largura: "))
h = int(input("Digite a altura: "))

n = 1
while n <= h:
    print("#", end="")
    f = 2
    
    while f < w:
        if n == 1 or n == h:
            print("#", end = "")
        else:
            print(end = " ")
        f = f + 1
        
    print("#")
    n = n + 1
