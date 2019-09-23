def main():
    num=0
    num=int(input("Numero par deseado: "))
    calculoPar(num);

def calculoPar(num):
    num=num
    nthPar=[]
    if(num>0):
       nthPar.append((num-1)*2)
    else:
        print("Ingrese numero mayor 0")
        num=int(input("Numero par : "))
        nthPar.append((num-1)*2)

    print("El ",num," numero par es ",nthPar)


main();
