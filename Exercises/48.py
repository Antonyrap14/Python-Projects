laptop = {
"P001":"laptop",
"P002":"smartphome",
"P003":"tablet",
"P004":"monitor",
}

laptop.pop("P003")
print(laptop)

#oppure
del laptop["P002"]
print(laptop)