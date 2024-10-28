""" Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes.
    Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
    Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, 
    usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? """

# A ideia eh deixar um dos interruptores ligado por um tempo maior e desligar, o segundo interruptor ligado, 
# e nunca ligar o terceiro. E entao verificar as outras salas uma vez e verificar
# qual lampada nao esta fria, e qual esta mais quente e uma fica acesa. Assim pode se resolver esse problema...

class Lampada:
    def __init__(self):
        self.acesa = False
        self.quente = False

    def ligar(self):
        self.acesa = True
        self.quente = True
    
    def desligar(self):
        self.acesa = False
        self.quente = True

class Sala:
    def __init__(self):
        self.lampada1 = Lampada()
        self.lampada2 = Lampada()
        self.lampada3 = Lampada()

    def ligar(self, indice):
        if indice == 1:
            self.lampada1.ligar()
        elif indice == 2:
            self.lampada2.ligar()
        elif indice == 3:
            self.lampada3.ligar()


    def desligar(self, indice: int):
        if indice == 1:
            self.lampada1.desligar()
        elif indice == 2:
            self.lampada2.desligar()
        elif indice == 3:
            self.lampada3.desligar()

    def verificar(self):
        estados = []
        contador = 1
        for lampada in [self.lampada1, self.lampada2, self.lampada3]:
            if lampada.acesa:
                estados.append((contador, "acesa"))
            elif lampada.quente:
                estados.append((contador, "apagada e quente"))
            else:
                estados.append((contador, "apagada e fria"))
            contador += 1
        return estados
    

sala = Sala()

sala.ligar(1)

sala.desligar(1)

sala.ligar(2)

estados = sala.verificar()

for indice, estado in estados:
    print(f"Lâmpada {indice} está {estado}")