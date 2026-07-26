number = float(input("inserisci un numero tra 0.0 e 1.0:"))

def valuation(number):
    
    if 0.9 <= number <= 1.0:
        print("A")
    elif 0.8 <= number < 0.9:
        print("B")
    elif 0.7 <= number < 0.8:
        print("C")
    elif 0.6 <= number < 0.7:
        print("D")
    else:
        print("F")

valuation(number)
