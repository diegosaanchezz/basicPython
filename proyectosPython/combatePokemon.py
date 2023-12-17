from random import randint as aleatorio
vidaPikachu = 80
vidaSquirtle = 90

while vidaPikachu > 0 and vidaSquirtle > 0:
    print('turno de pikachu')
    ataquePikachu = aleatorio(1,2)
    if ataquePikachu == 1:
        print('Pikachu ataca con bola voltio')
        vidaSquirtle -= 10
    else:
        print('Pikachu ataca con onda trueno')
        vidaSquirtle -= 10


    print('Turno squirtle')
    ataqueSquirtle = input('Que ataque deseas realizar? {P} placaje, {A} Pistola Agua, {B} Burbuja')
    if ataqueSquirtle == 'P':

    elif ataqueSquirtle == 'A':


