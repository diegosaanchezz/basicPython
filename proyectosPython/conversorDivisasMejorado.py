# programa de conversion entre divisas
print(""" Menu
            1. De Dolar a Euro 
            2. De Euro a Dolar
            3. De Libra a Euro 
            4. De Euro a Libra """)
opcion = int(input('Elige el tipo de conversion que deseas: '))

def DolarEuro():
    conversionDolarEuro = 0.91
    dolares = float(input('Ingrese la cantidad de dolares que desea cambiar: '))
    conversionRealizada = dolares * conversionDolarEuro
    print('Usted nos entrego {} dolares y sus euros son: {}'.format(dolares, conversionRealizada))

def EuroDolar():
    conversionEuroDolar = 1.08
    euros = float(input('Ingrese la cantidad de euros que desea cambiar: '))
    conversionRealizada = euros * conversionEuroDolar
    print('Usted nos entrego {} euros y sus dolares son: {}'.format(euros, conversionRealizada))

def libraEuro():
    conversionLibraEuro = 1.18
    libras = float(input('Ingrese la cantidad de libras que desea cambiar: '))
    conversionRealizada = libras * conversionLibraEuro
    print('Usted nos entrego {} libras y sus euros son: {}'.format(libras, conversionRealizada))

def euroLibra():
    conversionEuroLibra = 0.86
    euros = float(input('Ingrese la cantidad de euros que desea cambiar: '))
    conversionRealizada = euros * conversionEuroLibra
    print('Usted nos entrego {} euros y sus libras son: {}'.format(euros, conversionRealizada))

if opcion == 1:
    DolarEuro()
elif opcion == 2:
    EuroDolar()
elif opcion == 3:
    libraEuro()
elif opcion == 4:
    euroLibra()
else:
     print('La opcion que ingresaste es invalida')
     exit()