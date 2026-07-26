import datetime

def presta_libri(libro,nome,data=None):
    if data == None:
        data  = datetime.date.today()
    print(f"{libro},data{data},{nome}")

presta_libri("Pino","eraglaciale")
presta_libri("OLA","LOLA","2023-03-02")