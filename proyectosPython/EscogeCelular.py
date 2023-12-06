# Programa para que el usuario pueda escoger un celular
titulo = (' Bienvenido a este programa para que puedas escoger celular')
print(titulo, '\n', '-' * len(titulo), '\n')

pregunta1 = input('Quieres un celular con sistema operativo android o ios? ')

if pregunta1 == 'android':
    pregunta1android = input('Tienes dinero? ')
    if pregunta1android == 'no':
        print('Comprate un android chino de 100 euros')
    elif pregunta1android == 'si':
        pregunta2android = input('Te importa la camara del telefono? ')
        if pregunta2android == 'si':
            print('Comprate un Google Pixel Supercamara')
        elif pregunta2android == 'no':
            print('Comprate un android calidad precio')
        else:
            print('La opcion que ingresaste no es valida')
            exit()
    else:
        print('La opcion que ingresaste no es valida')
        exit()
elif pregunta1 == 'ios':
    pregunta1ios = input('Tienes dinero? ')
    if pregunta1ios == 'si':
        print('Comprate un iPhone Ultra Pro Max')
    elif pregunta1ios == 'no':
        print('Comprate un iPhone de segunda mano')
    else:
        print('La opcion que ingresaste no es valida')
        exit()
else:
    print('La opcion que ingresaste no es valida')
    exit()

