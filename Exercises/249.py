class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    
    def apply_discount(self,sconto=20):
        prezzo_scontato = self.price - ((self.price * sconto)/100)
        return prezzo_scontato
    @property
    def is_cheap(self):
        if self.price <20:
            return True
        else:
            return False
#MAIN
libro = Book("io","marra",100)
libro2 = Book("mino","peppe",19)
sconto = 50
print(libro.apply_discount())
print(libro.apply_discount(sconto))
print(libro2.is_cheap)
print(libro.is_cheap)
