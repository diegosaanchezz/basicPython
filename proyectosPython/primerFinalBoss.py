# Juego Escapa de la carcel!
import random
bienvenida = ('\nBienvenido al juego ESCAPA DE LA CARCEL!!!\n')
print(bienvenida + '-' * len(bienvenida))
print(""" 
        Instrucciones del juego:
        Se te estaran planteando diferentes casos en los cuales tendras que decidir y eso determinara
        si logras escapar de la carcel, eres capturado o mueres en el intento.""")
print("""
        Eres un prisionero y te encuentras en tu celda, has estado planeado en escapar y con herramientas que has 
        logrado robar del taller has logrado hacer un hoyo debajo de la cama pero los guardias sospechan de ti.\n 
""")
numeroPrisionero = random.randint(10000,3948493)
print('Prisionero con # {}, que planeas?'.format(numeroPrisionero))
print('Ultimamente has estado muy sospechoso')
preguntaPlaneando = input('No sera que estas planeado algo? ')
if preguntaPlaneando == 'si':
    print("""
    Revisaron tu celda y descrubrieron el hoyo que hiciste debajo de tu cama por lo tanto te transladaron a una
    celda de maxima seguridad y perdiste el juego """)
    exit()
elif preguntaPlaneando == 'no':
    print('mas te vale que no sea asi')
    eleccionEscape = int(input('Elige la forma de escape: \nPor el carrito de sabanas sucias(1) o Por el hoyo debajo de la cama(2): '))
    if eleccionEscape == 1:
        print('Escogiste el escape por el carrito de sabanas sucias ')
        numeroMultiplicar = random.randint(1,15)
        resultadoMultiplicacion = int(input("""\n
         Contesta correctamente la siguiente multiplicacion para desbloquear tu celda\n
         Cuanto es 8 x {} ? """.format(numeroMultiplicar)))
        resultadoMultiplicacionMaquina = numeroMultiplicar * 8
        if resultadoMultiplicacionMaquina == resultadoMultiplicacion:
            print('Has logrado desbloquear tu celda y has salido de tu cuarto \n Dirigiendote al cuarto de lavado...')
            decisionArmaTomar = int(input("""
                Has llegado al cuarto de lavado\n
                Ahi has encontrado un palo el cual te puede servir para defensa y dinero\n 
                Solo puedes llevar uno, esoge bien:
                1-Palo
                2-Dinero\n"""))
            if decisionArmaTomar == 1:
                decisionArmaTomar == 1
            elif decisionArmaTomar == 2:
                decisionArmaTomar == 2
            else:
                print('La opcion que has ingresado no es corrcta')
                exit()
            print("""
                    Has entrado al carrito y el encargado se dirige contigo a la camioneta 
                    que recoge las sabanas sucias
                    Se a ido el encargado y te has quedado solo con el encargado de la camioneta\n""")
            if decisionArmaTomar == 1:
                print('Has perdido por que puedes usar el palo para noquear al encargado pero los guardias te podran volver a capturar')
            elif decisionArmaTomar == 2:
                print('Has escogido el dinero y podras sobornar al encargado de la camioneta, Felicidades has ganado!')
            else:
                print('Has ingresado una opcion incorrecta')
                exit()
        else:
            print('No has acertado en la multiplicacion y has activado la alarma por lo tanto has perdido')
    elif eleccionEscape == 2:
        print('Escogiste el escape por el hoyo de la cama ')
        print("""
                 Has entrado al hoyo y estas en las alcantarillas, has caminado y cuando estas a punto de escapar te das cuenta
                 que hay una puerta la cual tiene una contraseña, la contraseña solo puede ser 1 o 2 pero cada cierto tiempo
                 la contraseña cambia asi que tienes 50% de equivocarte y que suene la alarma y 50% de lograr escapar de la carcel
                 """)
        respuestaCorrectaEscapeCama = random.randint(1,2)
        decisionEscapeCama = int(input('Deberas escoger bien, ingresa el numero (1) o (2): '))
        if decisionEscapeCama == respuestaCorrectaEscapeCama:
            print('Felicidades has adivinado la contraseña y has ganado el juego!')
        else:
            print('No has logrado adivinar, la contraseña era: {} y has activado la alarma\nPor lo tanto has perdido!'.format(respuestaCorrectaEscapeCama))
            exit()
    else:
        print('La opcion que ingresaste fue incorrecta')
        exit()
else:
    print('la opcion que ingresaste no es valida')