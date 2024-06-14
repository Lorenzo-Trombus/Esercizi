class Persona:
    def __init__(self,first_name:str,last_name:str):
        self.first_name=first_name
        self.last_name=last_name
        self.age=None
        if type(first_name) !=str:
            first_name=None
            return f"il nome inserito non è una stringa"
        elif type(last_name)!=str:
            last_name=None
            print("il cognome inserito non è una stringa")
        elif type(first_name) and type(last_name)==str:
            self.age=0
            

    
    def setName(self,first_name):
        if type(first_name)==str:
            self.first_name=first_name
        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self,last_name):
        if type(last_name)==str:
            self.last_name=last_name
        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self,age):
        if type(age)==int:
            self.age==age
        else:
            print("L'età deve essere un numero intero!")


    def getName(self):
        return self.first_name
    
    def getLastname(self):
        return self.last_name
    
    def getAge(self):
        return self.age
    
    def greet(self):
        print(f"ciao, sono {self.first_name} {self.last_name} e ho {self.age} anni")



    
        