def creaMail():
    nome = "antoo"
    dominio = "gmail"
    tld = "com"
    parts = [nome,dominio,tld]
    email = "@".join([nome,".".join([dominio,tld])])
  

    print(email)
creaMail()