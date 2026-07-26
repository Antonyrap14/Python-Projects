azioni ={
    "A":[10,-20,30,-22,-34,5],
    "B":[20,20,-21,-20,24,-30]
}

def mostra_aumenti(azioni):
        for azione,lista in azioni.items():
            print(f"\n{azione}\nvalori azione:")
            for valore in lista:
                if valore < -5:
                    continue
                else:
                    print(f"{valore}")

mostra_aumenti(azioni)
                


def get_stocks(market_data):
    for stock, price_changes in market_data.items():
        total_increase = sum(
            i for i in price_changes if i > 0
        )
        if total_increase >= 10:
            if all(i > -5 for i in price_changes):
                 print(stock)

market_data = {
    "ABC": [1, 2, 3, 4, 2, -6, 10],
    "DEF": [2, 3, 5, 6, 2, 4, 20],
    "GHI": [-2, -3, -5, -6, 2, 4, -20],
    "JKL": [10, 20, 30, 40, -5, 6, 7],
}

get_stocks(market_data)


