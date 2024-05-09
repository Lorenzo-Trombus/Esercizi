class Person:
    def __init__(self,name:str,surname:str,age:int):
        self.name= name
        self.surname=surname
        self.age=age
        #unca funzione che restituisce qualcosa senza return
#lorenzo = Person("lorenzo","Trombini",19)
#print(f"Nome={lorenzo.name},Cognome={lorenzo.surname},Età={lorenzo.age}")
"""name:str=input()
surname:str=input()
age:int=int(input())
person=Person(name,surname,age)
print(f"Nome={person.name},Cognome={person.surname},Età={person.age}")
"""        
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies:list[str]=[]
    """
    def add_hobbies(self,hobbies:str):
        self.hobbies.update(hobbies)
    
    def add_hobby(self,hobby:str):
        self.hobbies.add(hobby)

    def remove_hobby(self,hobby:str):
        self.hobbies.remove(hobby)
    """

    def __str__(self):
        return f"person(name={self.name},age={self.age},hobbies={self.hobbies})"


alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
lorenzo= Person("Lorenzo M.",21)
Danila= Person("Danila R.",21)
Oussama=Person("Oussama H.",10)
#alice.add_hobby("rugby")

people:list=[alice,bob,lorenzo,Danila,Oussama]
print(bob.name)
if bob.age<alice.age:
    print(alice.name)
else:
    print(bob.name)
i1=100000000000
name1:list=[]
for i in people:
    if i.age < i1:
        i1=i.age
        name1.append(i.name)

print(name1[-1])

class Student:
    def __init__(self,name,studyprogam):
        self.name=name
        self.studyprogram=studyprogam
        self.age=None
        self.gender=None
    
    def set_age(self,new_age):
        self.age=new_age
    
    def set_gender(self,new_gender):
        self.gender=new_gender

    def __str__(self):
        return f"name:{self.name},study program:{self.studyprogram},age:{self.age},gender:{self.gender}"
    

Io=Student("Lorenzo T.","Full Stack")
Lorenzo_M=Student("Lorenzo M.","Full Stack")
Manuel=Student("Manuel","Full Stack")
Lorenzo_M.age=300


print(Lorenzo_M)



class Animal:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs

    def setLegs(self,new_legs):
        self.legs=new_legs

    def getLegs(self):
        return self.legs

    def __str__(self):
        return f"name:{self.name}, number of legs: {self.legs}"

bat=Animal("bat",2)
wolf=Animal("wolf",4)
bat.legs-=1
bat.setLegs(2)
print(bat)

class Food:
    def __init__(self,name,price,description):
        self.name=name
        self.price=price
        self.description=description
    
    
    

lasagna=Food("lasagna",15,"ragù e besciamella avvolti da strati di pasta")
pizza=Food("lasagna",10,"impasto cotto al forno con sopra ingredienti a tua scelta")
carbonara=Food("carbonara",17,"pasta con crema di uova e pecorino con guanciale e pepe")


class Menu:
    def __init__(self,Foods:list=[]):
        self.Food=Foods

    def addFood(self,food:Food):
        self.Foods.append(food)

    def remove_food(self,food:Food):
        if food in self.Foods:
            self.Foods.remove(food)

    def __str__(self):
        repr:str=""
        for food in self.Foods:
            repr+= "\n" + str (food)
        return repr[1:]

menu=Menu(carbonara)
print(carbonara)

"""
class Restaurant:
    
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"Restaurant={self.name}, cuisine={self.cuisine_type}")

    def open_restaurant(self):
        print(F"Il ristorante {self.name} è aperto")

    def set_number_served(self,new_number_served):
        self.number_served=new_number_served

    def increment_number(self):
        self.number_served+=1

    def clean(self):
        self.number_served=0

r1=Restaurant(name="la vecchia roma",cuisine_type="Romana",number_served=100)

print(r1.open_restaurant())
print(r1.describe_restaurant())
print()

class user:
    def __init__(self,
                 first_name,
                 last_name,
                 age,
                 Cf,
                 email):
        self.first_name=first_name
        self.Last_name=last_name
        self.age=age
        self.Cf=Cf
        self.email=email

    def __str__(self):
        return f""

"""        

class Persona:

    def __init__(self,name:str,cognome:str,data_di_nascita:str,genere:str)->None:
        self.nome:str=name
        self.cognome:str=cognome
        self.data_di_nascita:str=data_di_nascita
        self.genere:str=genere

    def calcola_età(self):
        return 10

persona_1:Persona= Persona(name="Lorenzo",cognome="Trombini",data_di_nascita="27/02/05",genere="Maschio")

class Dipendente(Persona):
    def __init__(self, name: str, cognome: str, data_di_nascita: str, genere: str,ore_lavorate:int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere)

        self.ore_lavorate:int=ore_lavorate

    def calcola_stipendio(self):
        return 500.0

dipendente1: Dipendente= Dipendente(name="Lorenzo",cognome="Trombini",data_di_nascita="27/02/05",genere="Maschio",ore_lavorate=500)

class Professore(Dipendente):
    def __init__(self, name: str,
                  cognome: str, 
                  data_di_nascita: str, 
                  genere: str, 
                  ore_lavorate: int,
                  materia_insegnata:int,
                  ore_di_lezione:int) -> None:
        super().__init__(name, cognome, data_di_nascita, genere, ore_lavorate)

        self.materia_insegnata:str=materia_insegnata
        self.ore_di_lezione:int=ore_di_lezione

    def __str__(self) -> str:
        return f"professor {self.nome} {self.cognome}"

print(persona_1.calcola_età())

print(dipendente1.nome)
print(dipendente1.calcola_età())
print(dipendente1.ore_lavorate)
professore1:Professore=Professore(name="Lorenzo",cognome="Trombini",data_di_nascita="27/02/05",genere="Maschio",ore_lavorate=500,materia_insegnata="italiano",ore_di_lezione=30)
print(professore1.ore_di_lezione)
print(str(professore1))  


  




#https://github.com/flaat/its.git
