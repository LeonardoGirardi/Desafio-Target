"""Descubra a lógica e complete o próximo elemento:
b) 2, 4, 8, 16, 32, 64, ___"""

def sequencia_logica(index: int) -> list:
    arr = []
    i = 0
    aux = 2 # numero inicial
    while i != index:
        arr.append(aux)
        aux = aux * 2
        i += 1
    return arr

#Nessa logica, cada numero eh o dobro do seu antecessor

print(sequencia_logica(7))