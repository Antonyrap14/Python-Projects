def BMI(peso:float,altezza:float) -> float:
    bmi = peso / altezza**2
    return bmi

def risposta(bmi:float) -> str:
    if bmi < 18.5:
        return "sottopeso"
    elif 18.5 <= bmi < 25:
        print("normale")
    elif 25 <= bmi < 30:
        print("sovrappeso")
    else:
        print("obeso")
 
bmi = BMI(90,1.75)
print(bmi)
print(risposta(bmi))