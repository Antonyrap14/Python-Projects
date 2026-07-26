class Animale:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    
    def info(self):
        return f"{self.nome},{self.eta}"

class Mammifero(Animale):
    def __init__(self, nome, eta,manto):
        super().__init__(nome, eta)
        self.manto = manto
    
    def info(self):
        super().info()
        return f"{super().info()},{self.manto}"

class Uccello(Animale):
    def __init__(self, nome, eta,specie):
        super().__init__(nome, eta)
        self.specie = specie
    
    def info(self):
        return f"{super().info()},{self.specie}"

pesce = Animale("pesce",22)
print(pesce.info())        

mamma = Mammifero("mamma",52,"bianco")
print(mamma.info())

uccello = Uccello("uccello",2,"piccione")
print(uccello.info())