# generiamo una lista di numeri casuali
import random

random_numbers = [
    random.randint(1, 100)
    for _ in range(1, 50)
]

def conta_numero(lista,):
    numero = int(input("Scrivi un numero"))
    count = 0
    for n in lista:
        if numero == n:
           count += 1
    print(f"Il numero compare {count} volte")

conta_numero(random_numbers)
print("\n",random_numbers)


nu = [
    random.randint(1,200)
    for _ in range (1,10)
]
print(nu)