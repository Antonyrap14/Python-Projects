import random
chiamate = 0
count = 0

while chiamate <= 120:
    chiamate += 1
    risposta = random.choice([True,False])

    if risposta == True:
        count += 1
    
if count > 50:
    print(f"complimenti hai raggiunto le 50 chiamate in {count} tentativi")
else:
    print(f"Ci hai provato {count}")

