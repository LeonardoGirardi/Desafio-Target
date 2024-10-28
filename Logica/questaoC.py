""" Descubra a lógica e complete o próximo elemento:
c) 0, 1, 4, 9, 16, 25, 36, ____"""

#A logica desse programa eleva o numero de 1 a 8 ao quadrado

def sequencia_logica(index: int) -> list:
    arr = []
    i = 0
    while i != index:
        aux = i ** 2
        arr.append(aux)
        i += 1
    return arr

print(sequencia_logica(8))