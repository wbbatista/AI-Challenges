def calculo_prefixo(entrada1,entrada2):


    e1 = list(entrada1)
    e2 = list(entrada2)

    tam1 = len(entrada1)
    tam2 = len(entrada2)

    cont = min(tam1,tam2)

    a = 0

    for x in range(cont):
        if e1[x] == e2 [x]:
            a += 1
        else: break

    return a
