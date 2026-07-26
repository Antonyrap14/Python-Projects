class Animale:
    def __init__(self,nome:str,eta:int):
        self.nome = nome
        self.eta = eta
    
    def carateristic(self):
        return f"Nome:{self.nome}\nEta:{self.eta}\n"

class Leone(Animale):
    def ruggire(self):
        return f"Il leone {self.nome} di eta {self.eta} sta ruggendo!"

class Pinguino(Animale):
    def cammina(self):
        return f"Il pinguino {self.nome} sta camminando!"

    def nuota(self):
        return f"Il pinguino {self.nome} sta nuotando!"        

leone = Leone("Pino",43)
print(leone.ruggire())

pinguino0 = Pinguino("Pingu",20)
pinguino1 = Pinguino("Lino",10)
print(pinguino0.cammina())
print(pinguino1.nuota())
print(leone.carateristic())
print(pinguino0.carateristic())
print(pinguino1.carateristic())