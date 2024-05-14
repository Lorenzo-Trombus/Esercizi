class Zoo:
    

class Fence(Zoo):
    def __init__(self,area:float,temperature:float,habitat:str):
        super().__init__()
        self.area=area
        self.temperature=temperature
        self.habitat=habitat

class Animal(Zoo):
    def __init__(self,name:str,species:str,age:int) -> None:
        super().__init__()
        self.name=name
        self.species=species
        self.age=age
    


class ZooKeeper(Zoo):
    def __init__(self,name: str, surname:str, id:int ):
        self.name=name
        self.surname=surname
        self.id=id


