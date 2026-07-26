temperatures_fahrenheit = [32, 212, 77, 104, 0, -40]

def converti(lista):
    print(f"Gradi Fahrenheit:\n{lista}")
    celsius = [
        round((5/9)*(grado-32),2) for grado in lista 
    ]
    print(f"Gradi Celsius:\n{celsius}")

converti(temperatures_fahrenheit)



