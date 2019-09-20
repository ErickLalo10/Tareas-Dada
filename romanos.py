def convertir():
    for i in range (1, 3901):
        arabigo = int(i)
        romano = ""
        romanoAbec=[[1000,900,500,100,90,50,40,10,9,5,4,1],['M','CM','D','C','XC','L','XL','X','IX','V','IV','I']]

        for i in range(len(romanoAbec[0])):
            if (arabigo // romanoAbec[0][i]>=1):

                romano+= arabigo // romanoAbec[0][i] * romanoAbec[1][i]
                arabigo-= arabigo // romanoAbec[0][i] * romanoAbec[0][i]
        print(romano)

def main():
    convertir()

if __name__ == '_main_':
    main()