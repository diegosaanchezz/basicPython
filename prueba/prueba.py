import os
import platform

def check_python():
    try:
        # Verificar si Python está instalado
        python_version = os.popen('python --version').read().strip()
        print(f'Python version: {python_version}')

    except FileNotFoundError:
        # Si no se encuentra Python, intentar instalarlo
        print('Python no encontrado. Intentando instalar...')

        if platform.system() == 'Windows':
            os.system('choco install python -y')  # Requiere Chocolatey en Windows

        elif platform.system() == 'Linux':
            os.system('sudo apt-get update && sudo apt-get install python3 -y')  # APT en Linux

        elif platform.system() == 'Darwin':
            os.system('brew install python')  # Requiere Homebrew en macOS

        else:
            print('No se pudo determinar el sistema operativo. Por favor, instala Python manualmente.')

if __name__ == "__main__":
    check_python()

# Resto del código de tu script Python
n = 1
while True:
    n += 1
    print(n)
