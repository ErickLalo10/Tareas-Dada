import random 

def busqueda(arreglo,num):
    veces=0
    suma=[]
    for i in range(len(arreglo)):
        if(arreglo[i]==num):
            suma.append(i)
            veces+=1
    return suma,'Repeticiones: ',veces

lista=[random.randint(0,100) for i in range(10000)]
print("7: ",busqueda(lista,7),"\n\n\n\n")
print("99: ",busqueda(lista,99),"\n\n\n\n")
print("101: ",busqueda(lista,101),"\n\n\n\n")
print("44: ",busqueda(lista,44),"\n\n\n\n")
