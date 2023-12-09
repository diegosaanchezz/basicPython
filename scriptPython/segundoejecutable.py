import subprocess
import codigo

# Ejecutar la función desde codigo.py
codigo.funcionPrincipal()

# Ejecutar comandos en la terminal
try:
    # Abrir el archivo usando exec y redirigir la salida a file
    subprocess.run('exec 5<> file', shell=True, check=True)

    # Ejecutar el comando python ejecutable.py y redirigir la salida a 5
    subprocess.run('python ejecutable.py >&5', shell=True, check=True)

except subprocess.CalledProcessError as e:
    print(f'Error al ejecutar comandos en la terminal: {e}')
