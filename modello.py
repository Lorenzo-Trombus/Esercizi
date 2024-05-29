class Banca:

    def __init__(self,nome:str,simbolo:str):
        self.nome=nome
        self.simbolo=simbolo
        self.lista_filiali:list[Filiale]=[]

class Filiale:
    
    def __init__(self,codice:str,indirizzo:str,banca:Banca):
        
        self.codice=codice
        self.indirizzo=indirizzo
        self.banca=banca

unicredit=Banca(nome="Unicredit",simbolo="UCG")
intesa:Banca=Banca(nome="Intesa San Paolo",simbolo="ISP")
filiale_unicredit_1=Filiale(codice="UCG01",
                            indirizzo="Via Sierra nevada, 60, Roma, Italia",
                            banca=unicredit)


unicredit.lista_filiali

print(filiale_unicredit_1.banca.nome)
