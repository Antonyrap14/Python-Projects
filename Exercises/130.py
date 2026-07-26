lista = [1,2,4,2,3,1,3,4,8,6]

new_list = []
for prodotto in lista:
    if prodotto not in  new_list:
        new_list.append(prodotto)
    else:
        continue

count = 0
for elementi in new_list:
    count += 1
    
print("Il totale degli elementi è:{0}".format(count))
            

        
       

        
        

