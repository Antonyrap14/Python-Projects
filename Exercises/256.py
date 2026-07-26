class User:
    avaiable_idrs = ()
    next_id = 1

    @staticmethod
    def next_id(self):
        if self.avaiable_idrs:
            return self.avaiable_idrs.pop()
        else:
            next_id += 1
            return next_id - 1
        
    def __init__(self):
        self.id = User.next_id()


utente = User()
print(f"User:{utente.id}")



        