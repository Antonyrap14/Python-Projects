dataset = [1,2,22,33,55,51,20,34,37,38,39,40,11]

def numeri_pari(dataset):
    new_list = [
        element for element in dataset if element % 2 == 0
    ]
    print(new_list)

numeri_pari(dataset)