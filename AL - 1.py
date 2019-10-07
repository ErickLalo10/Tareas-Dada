def primos(p):
    primos=[]
    noPrimos=[]
    j=0
    for i in range(2,p):
        if(i%2==0):
            primos.append(i)
        else:
            noPrimos.append(i)
    print(primos)
    print(noPrimos)

        

numElement=int(input("¿Hasta que numero quiere que lo numeros primos?"))
primos(numElement)
