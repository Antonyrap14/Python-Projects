email = {'alice@example.com', 'bob@example.com', 'carol@example.com'}

def aggiungi(email,mail):
    email.add(mail)

lista = ['dave@example.com', 'bob@example.com','bob@example.com']
for elemento in lista:
    aggiungi(email,elemento)
print(email)