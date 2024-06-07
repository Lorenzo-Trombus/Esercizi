"""
Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) 
e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, 
aggiungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto, 
3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, 
il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, 
saggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().


"""

class Media:
    def __init__(self,title:str,review:list[int]=[]) -> None:
        self.title=title
        self.review=review

    def set_title(self, title): 
        self.title=title

    def get_title(self):
        return self.title

    def aggiungiValutazione(self,voto:int):
        if 1<=voto<=5 and type(voto)==int:
            self.review.append(voto)

    def getMediaValutazioni(self):
        return sum(self.review)/len(self.review)
    
    def getRate(self):
        if sum(self.review)/len(self.review)<=1.5:
            return f"Terribile"
        elif 1.5<sum(self.review)/len(self.review)<=2.5:
            return f"Brutto"
        elif 2.5<sum(self.review)/len(self.review)<=3.5:
            return f"Normale"
        elif 3.5<sum(self.review)/len(self.review)<=4.5:
            return f"Bello"
        elif 4.5<sum(self.review)/len(self.review)<=5:
            return f"Grandioso"
        
    def ratePercentage(self,voto:int):
        lista_voto=[]
        for voto in self.review:
            lista_voto.append(voto)

        return f"{(len(lista_voto)*100)/len(self.review)}%"
    
    def recensione(self):
        return f"Titolo:{self.title}, voto medio: {self.getMediaValutazioni()},Giudizio:{self.getRate()},
        Percentuali:boh"




class Film(Media):
    def __init__(self, title: str, review: list[int]) -> None:
        super().__init__(title, review)


