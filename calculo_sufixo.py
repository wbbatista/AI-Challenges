def calculo_sufixo (string1):

    e1 = list(string1)
    e2 = list(string1)

    b = 0
    c = 0

    it = len(entrada1)
    for x in range(it):
        tam = len(e2)
        if tam == 0: break
        else: 
            b = calculo_prefixo(e1,e2);
            c += b;
        e2.pop(0)  
        
    return string1,c

