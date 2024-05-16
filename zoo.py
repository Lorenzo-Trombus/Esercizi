class Animal:
    def __init__(self,name:str,species:str,age:int, height:float, width:float, preferred_habitat:str, health:float ):
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.health=health
        self.area_an=height*width

    def area_animale(self,height:float,width:float):
        self.area_an=height*width

class Fence:
    def __init__(self,area:float,temperature:float,habitat:str):
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.area_rimanente= self.area - self.area_occupata




class ZooKeeper:
    def __init__(self,name: str, surname:str, id:int ):
        self.name=name
        self.surname=surname
        self.id=id
    
    def add_animal(self,animal:Animal,fence:Fence):
        if fence.area_rimanente>=
    def remove_animal(self,animal: Animal, fence: Fence):
        pass    

    def feed(self,animal: Animal):
        pass

    def clean(self,fence: Fence):
        pass


class Zoo:
    def __init__(self):
        pass
    def describe_zoo(self):
        #print(f"nello zoo ci sono {len(fence.fences)} recinti,{len(zookeper.zookeepers)} custodi e {len(animal.animals)} animali")
    
        pass



    
    















