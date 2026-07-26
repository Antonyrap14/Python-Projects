text = "Il presidente John Doe e il primo ministro Jane Smith si sono incontrati oggi."
dictionary = {"John Doe": "Presidente degli Stati Uniti", "Jane Smith": "Primo Ministro del Regno Unito"}

def replace(text,dictionary):
    for key,value in dictionary.items():
        text = text.replace(key,value)
    return text

print(replace(text,dictionary))

