def multiplicacion(lista):
    res=0
    if (len(lista)>0):
        res=lista[0]
        for i in range(1,len(lista)):
            res*=lista[i]
        return res
    else:
        print("El arreglo debe contener algo")

def main():
    lista=[1,2,3,4]
    print(lista,multiplicacion(lista))

if __name__=='__main__':
    main();