
# Avete una lista di studenti con i relativi voti di un esame.
#  La lista si presenta come segue:
#  studentivoti = [(’Mario’, 88), (’Luigi’, 92), (’Peach’, 85), (’Bowser’, 76), (’Wario’, 90)].

#  Il vostro obiettivo è di riorientare questa lista in base ai voti degli studenti,
#  dal più alto al più basso. Dopo l’ordinamento, la lista dovrebbe apparire come
#  [(’Luigi’, 92), (’Wario’, 90), (’Mario’, 88), (’Peach’, 85), (’Bowser’, 76)]

studentivoti = [("Mario", 88), ("Luigi", 92), ("Peach", 85), ("Bowser", 76), ("Wario", 90)]

def riordina(lista):
    studentivoti.sort(key=lambda x:x[1], reverse=True)
    print(lista)

riordina(studentivoti)