stringa = ["Ciao", "a", "tutti", "!", "Benvenuti", "alla", "nostra", "newsletter"]

def parse(stringa):
    text = " ".join(stringa)
    return f"<p>{text}<p>"

print(parse(stringa))

