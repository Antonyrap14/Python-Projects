# Siete gestori di un cinema e avete una lista di film già programmata per la giornata.
#  A causa di richieste del pubblico, dovete inserire un film extra nella vostra programmazione.
#  Il film extra deve essere messo al terzo posto nella vostra lista di film.
#  La vostra lista iniziale di film è 
# [’Avengers’, ’Batman’, ’Superman’, ’Ironman’, ’Spiderman’].
#  Il film extra da inserire è ’Hulk’.
#  Scrivete un programma Python che utilizza il metodo insert() per aggiungere ’Hulk’ al terzo posto 
# nel vostro elenco di film.

film = ["Avengers","Batman","Superman","Ironman","Spiderman"]

film.insert(2,"Hulk")

print(film)