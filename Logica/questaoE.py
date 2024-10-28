"""Descubra a lógica e complete o próximo elemento:
e) 1, 1, 2, 3, 5, 8, ____"""

# A logica eh igual a sequencia de fibonacci, o proximo eh igual a soma dos 2 anteriores

def sequencia_logica(index: int) -> list:
    arr = []
    i = 0
    a, b = 0, 1
    while i != index:
        a = a + b
        b = a - b 
        arr.append(b)
        i += 1
        
    return arr

print(sequencia_logica(8))




