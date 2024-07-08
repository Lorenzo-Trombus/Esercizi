class Documento():
    def __init__(self,testo:str) -> None:
        self.testo=testo
        

    def getText(self):
        return self.testo
    
    def setText(self,text):
        self.testo=text

    def isInText(self,keyword):
        if keyword in self.testo:
            return True
        
    
class Email(Documento):

    def __init__(self, testo: str,mittente:str,destinatario:str, titolo_messaggio) -> None:
        super().__init__(testo)
        self.mittente=mittente
        self.destinatario=destinatario
        self.titolo_messaggio=titolo_messaggio


    def getMittente(self):
        return self.mittente
    
    def getDestinatario(self):
        return self.destinatario
    
    def getTitolo(self):
        return self.titolo_messaggio
    
    def setMittente(self,mitt):
        self.mittente=mitt

    def setDestinatario(self, dest):
        self.destinatario=dest

    def setTitolo(self, titolo):
        self.titolo_messaggio=titolo

    def getTesto(self):
        return self.testo
    

documento1=Documento(testo="lecca lecca senza gengive")
email1=Email(testo=documento1.testo,mittente="Pippo",destinatario="Baudo",titolo_messaggio="aiuto aiuto")

print(email1.getTesto())
    
