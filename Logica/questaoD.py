""" Descubra a lógica e complete o próximo elemento:
4, 16, 36, 64, ____"""

# A sequencia representa o quadrado dos numeros pares
# Comecando por 2 

def sequencia_logica(index: int) -> list:
    arr = []
    aux, i = 2, 0

    while i != index:
        arr.append(aux**2)
        aux += 2
        i += 1
    return arr


print(sequencia_logica(5))