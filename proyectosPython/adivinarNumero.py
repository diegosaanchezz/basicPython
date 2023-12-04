import random
numeroAdivinar = random.randint(1,10)
numeroElegido = int(input('Dime un numero del 1 al 10: '))
if numeroElegido >= 1 and numeroElegido <= 10:
        if numeroElegido == numeroAdivinar:
            print('Felicidades adivinaste el numero!')
        else:
            print('Lo siento no adivinaste el numero')
            print('El numero a adivinar era: {}'.format(numeroAdivinar))
else:
    print('No ingresaste un numero en el rango indicado')