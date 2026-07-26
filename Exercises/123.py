tariffa = int(input("scrivi tariffa:"))

def delivery(price):
    if price >= 50:
        print("free delivery")
    else:
        print("You will pay 5 euro for delivery")

delivery(tariffa)