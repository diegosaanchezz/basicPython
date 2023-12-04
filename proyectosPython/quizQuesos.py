titulo = "Bienvenido a esta encuesta para saber cuanto te gustan los quesos"
print(titulo + '\n' + len(titulo) * '-' + '\n')
#PREGUNTA 1------------------------------------------------------
puntuacion = 0
opcion = input("""Pregunta 1: que haces cuando ves una tabla de quesos?
                A = salgo corriendo 
                B = pruebo uno de los quesos o incluso varios 
                C = no puedo evitar devorarla \n""")
if opcion == 'A':
    puntuacion = puntuacion
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 10
else:
    print('La opcion que ingresaste no fue correcta')
    exit()
print(puntuacion)
#FINAL PREGUNTA 1---------------------------------------------------
# PREGUNTA 2--------------------------------------------------------
opcion = input("""Pregunta 2: como te gusta la hamburguesa?
                  A = sin queso
                  B = con queso 
                  C = pan y queso \n""")
if opcion == 'A':
    puntuacion = puntuacion
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 10
else:
    print('La opcion que ingresaste no fue correcta')
    exit()
print(puntuacion)
# FINAL PREGUNTA 2-------------------------------------------------
# PREGUNTA 3-------------------------------------------------------
opcion = input("""pregunta 3: eres intolerante a la lactosa?
                  A = Si 
                  B = A veces
                  C = no \n""")
if opcion == 'A':
    puntuacion = puntuacion
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 10
else:
    print('La opcion que ingresaste no fue correcta')
    exit()
print(puntuacion)
# FINAL PREGUNTA 3-------------------------------------------------

if puntuacion >= 0 and puntuacion < 15:
    print('Tu puntuación es: {} por lo tanto no te gusta el queso'.format(puntuacion))
elif puntuacion >= 15 and puntuacion < 25:
    print('Tu puntuacion es: {} por lo tanto te gusta el queso'.format(puntuacion))
elif puntuacion >= 25 and puntuacion <= 30:
    print('Tu puntuacion es: {} por lo tanto te encanta el queso'.format(puntuacion))
else:
    print('Ocurrio un error en la puntuacion, por favor intentalo de nuevo')