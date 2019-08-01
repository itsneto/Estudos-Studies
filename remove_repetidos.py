def remove_repetidos(list):
    x = []
    for i in list:
        repetido = False
        for n in x:
            if i == n:
                repetido = True
                break
        if repetido == False:
            x.append(i)
    return sorted(x)
