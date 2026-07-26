class Veicolo:
    def __init__(self,marca,modello):
        self.marca = marca
        self.modello = modello
    
    def stamp(self):
        return f"Brand:{self.marca}\nModel:{self.modello}"

class Auto(Veicolo):
    def __init__(self, marca, modello,numero_posti):
        super().__init__(marca, modello)
        self.numero_posti = numero_posti
    def stamp(self):
        return f"{super().stamp()}\nNumero di posti:{self.numero_posti}"

class Moto(Veicolo):
    def __init__(self, marca, modello,colore):
        super().__init__(marca, modello)
        self.colore = colore
    
    def stamp(self):
        return f"{super().stamp()}\nColore:{self.colore}"
    

auto = Auto("Ferrari","F40",2)
print(auto.stamp())

moto = Moto("Yamaha","R12","Verde fluo")
print(moto.stamp())