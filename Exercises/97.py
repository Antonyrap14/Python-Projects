archive = "pane, pasta, vino, acqua, Lind"
product = "Lind"

def search(archive,product):
    list = []
    a = archive.lower()
    archive_list = a.split(", ")
    product = product.lower()

    for element in archive_list:
        if element == product:
            list.append(element)
        print(list)

search(archive,product)