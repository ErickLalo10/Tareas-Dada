def divisiblePor(arr,div):
    nueva=[]
    for i in range (0,len(arr)):
        if(arr[i]%div==0 and arr[i]!=0):
            nueva.append(arr[i])
    return nueva

total=int(input("¿Cuantos elementos desea ingresar? "))
lista=[]
for i in range (0,total):
    lista.append(int(input(f"Introduzca un numero para la posicion {i}: ")))
divisor=int(input("Digite el divisor: "))
print(divisiblePor(lista,divisor))
