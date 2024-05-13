# APPUNTI LEZIONE 8
class Animal:
    def __init__(self,species:str,age:int):
        self.species=species
        self.age=age

    def __str__(self) -> str:
        return f"{self.__class__.__name__}, species={self.species}, age={self.age} " 
                 
class Person (Animal):
    def __init__(self,name:str,surname:str,cf:str, species: str, age: int):
        super().__init__( age,species)
        self.name=name
        self.cf=cf
        self.surname=surname

    def __str__(self) -> str:
        s:str= super().__str__()[:-1]
        s += f"{self.name},{self.surname},cf={self.cf}"
    
    


class Student(Person):
    def __init__(self, species: str, age: int, name: str,surname:str, cf: str, matricula:int):
        super().__init__(species, age, name,surname, cf)
        self.matricula=matricula
    


class Cat(Animal):
    def __init__(self, species: str, age: int, name:str):
        super().__init__(species, age)
        self.name=name


class Rabbit(Animal):
    def __init__(self, species: str, age: int, name:str):
        super().__init__(species, age)
        self.name=name


lore=Person(species="umano",age=19,name="lorenzo",surname="trombini",cf="LSFJFSDFBVKJS")
print(lore)


class Room:
    def __init__(self,id:str,floor:int,seats:int):
        self.id=id
        self.floor=floor
        self.seats=seats

    def __str__(self):
        return f"Room(id={self.get_id()},floor={self.get_floor()},seats={self.get_seats()})"

class Building:
    def __init__(self,name:str,address:str,num_floors:int,rooms:list=[]):
        self.name=name
        self.address=address
        self.rooms=rooms
        self.num_floors=num_floors

    def get_num_floors(self):
            return self.num_floors()

    def get_rooms(self):
        return self.rooms

    def add_room(self,room:Room):
        if room not in self.rooms and room.get_floor()<=self.get_num_floors():
            self.rooms.append(room)

    def __str__(self) -> str:
        return f"{self.name.capitalize()} @ {self.address}"
    

# INCOMPLETO