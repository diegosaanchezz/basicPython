print('Me voy a la cocina')
print('abro la nevera')

hayLeche = input("Hay leche? si o no?")
hayColacao = input('Hay colacao? si o no?')

if hayLeche != 'si' or hayColacao != 'si':
    print('voy al super')
    if hayLeche != 'si':
        print('Voy a comprar leche')
    if hayColacao != 'si':
        print('Voy a comprar colacao')

print('esta listo')