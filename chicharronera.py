21 lines (19 sloc)  661 Bytes
 
print("Quadratic Equation Solver\n");
a=float(input('Valor de coeficiente cudrático: '))
b=float(input('Valor de coeficiente lineal: '))
c=float(input('Valor de término independiente: '))
def ecu(a,b,c):
    dis=(b*b)-(4*a*c)
    if(dis>0):
        x1=(-b+((dis)**(1/2)))/(2*a)
        x2=(-b-((dis)**(1/2)))/(2*a)
        print("\nX1= ",x1,"\nX2= ",x2)
    if(dis==0):
        x1=x2=(-b)/(2*a)
        print("\nX1 = "+str(x1)+"\nX2 = "+str(x2))
    if(dis<0):
        xr=(-b)/(2*a)
        x1=((-dis)**(1/2))/(2*a)
        x2=-(-dis)**(1/2)/(2*a)
        print("\nX1 real=",xr,"X1 imaginaria= j",x1,"\nX2 real=",xr,"X2 imaginaria= j",x2)
        
ecu(a,b,c)