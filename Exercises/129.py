tempi = ["23", "21", "27", "22", "25", "24", "26", "24", "27"]

temp = len(tempi)
somma = 0

for elementi in tempi:
    somma += int(elementi)

media = somma / temp
print(media)


