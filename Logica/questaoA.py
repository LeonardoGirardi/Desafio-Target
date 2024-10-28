"""Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___"""

#Trata-se de uma sequencia de numeros impares

def sequencia_logica(index: int) -> list:
    arr = []
    i = 0
    aux = 1
    while i != index:
        arr.append(aux)
        aux = aux + 2
        i += 1
    return arr

#Descobrir o quinto Elemento, portanto inserir Index = 5
print(sequencia_logica(5))

