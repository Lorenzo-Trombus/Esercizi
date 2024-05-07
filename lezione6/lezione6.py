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

