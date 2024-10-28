"""Descubra a lógica e complete o próximo elemento:
f) 2,10, 12, 16, 17, 18, 19, ____"""

def sequencia_logica(index: int) -> list:
    arr = [2]
    k = [2, 8, 4, 1, 1, 1] # Incrementos

    for i in range(1, index):
        elemento = arr[-1] + (k[i - 1] if i - 1 < len(k) else 1)
        arr.append(elemento)
        print(elemento)

    return arr   

print(sequencia_logica(8))