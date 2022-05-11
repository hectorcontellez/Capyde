from random import shuffle

# Lista Inicial
palitos = ['-','--','---','----']

# Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# Pedir al usuario intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3',4]:
        intento = input('[>] Elige un número del 1 al 4: ')
    return int(intento)

# Comprobar el intento
def checar_intento(lista, intento):
    if lista[intento -1] == '-':
        print('Perdite')
    else:
        print("Esta vez te has salvado")
    
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)

seleccion = probar_suerte()

checar_intento(palitos_mezclados, seleccion)