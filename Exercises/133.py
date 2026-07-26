def tasso_interesse():

        p = int(input("inserisci p"))
        n = int(input("inserisci n"))
        t = int(input("inserisci t"))    
       
        while(True):
            r = float(input("inserisci r"))
            if (0 <= r <= 1):
                tasso = (p*(1+r/n))**(n*t)
                print(f"{tasso}")
                break
        


tasso_interesse()

