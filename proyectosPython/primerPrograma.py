# Programa en el cual el usuario pueda ingresar tres numeros y nos diga cual es el numero mas grande y mas chico
class pedirNumeros:
         def pedirDatos(self):
            self.primerNumero = int(input('Ingresa el primer numero: '))
            self.segundoNumero = int(input('Ingresa el segundo numero: '))
            self.tercerNumero = int(input('Ingresa el tercer numero: '))
         def numeroMayor(self):
             self.numeroMasGrande = max(self.primerNumero, self.segundoNumero, self.tercerNumero)

         def numeroMenor(self):
            self.numeroMasChico = min(self.primerNumero, self.segundoNumero, self.tercerNumero)

         def imprimirinfo(self):
            print("El numero mas grande es: {} y el numero mas chico es: {}".format(self.numeroMasGrande, self.numeroMasChico))

objeto = pedirNumeros()
objeto.pedirDatos()
objeto.numeroMayor()
objeto.numeroMenor()
objeto.imprimirinfo()
