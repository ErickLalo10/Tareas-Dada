lista=[5,8,3,2,1,9,3,4,2,4,6,7,9,12,45,23,14,54,12,13,18]

def suma_pares():
    temp=0
    for i in range(0, len(lista)):
        if lista[i]%2==0:
            temp=lista[i]+temp
    return temp

def elevar_nones():
    arr=[]
    for i in range(0, len(lista)):
        if lista[i]%2!=0:
            arr.append(lista[i]*lista[i])
    return arr

def main():
    print("Suma pares: \n",suma_pares())
    print("Lista de nones al cuadrado: \n",elevar_nones())

main();