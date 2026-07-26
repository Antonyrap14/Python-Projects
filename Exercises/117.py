def category(donazione):
    if donazione < 100:
        print("Cane")
    elif 100 <= donazione < 500:
        print("Orso")
    elif 500<= donazione < 1000:
        print("Tigre")
    else:
        print("Leone")
a = int(input("inserisci prezzo:"))
category(a)