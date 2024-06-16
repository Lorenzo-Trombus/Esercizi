from persona import Persona



class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, idCode:str):
        super().__init__(first_name, last_name)
        self.idCode=idCode

    def setIdCode(self,idCode:str):
        if type(idCode)==str:
            self.idCode = idCode


    def getIdCode(self):
        return self.idCode
    
    def patientInfo(self):
        print(f"Paziente: {self.first_name} {self.last_name}\n ID: {self.idCode}")
            
    