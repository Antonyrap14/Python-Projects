# Immaginate di essere un insegnante che sta inserendo i voti dei suoi studenti in un registro online.
#  Ogni voto viene inserito in una lista in ordine cronologico. Tuttavia, avete accidentalmente dimenticato di
#  inserire il voto di un test di un particolare studente che è stato fatto prima degli altri.
#  Il vostro compito è di inserire questo voto mancante nella posizione corretta senza dover riorganizzare tutta 
# la lista dei voti. I voti esistenti corrispondono ai seguenti: [18, 20, 24, 25, 22].
#  Il voto mancante è 23 e deve essere inserito tra 20 e 24.

voti = [18, 20, 24, 25, 22]
voto_mancante = 23
voti.insert(2,voto_mancante)
print(voti)

# soluzione proposta
# Lista dei voti esistenti
grades = [18, 20, 24, 25, 22]

# Voto mancante
missing_grade = 23

# Posizione del voto mancante
pos = grades.index(24)

# Inserire il voto mancante
grades.insert(pos, missing_grade)

print(grades)