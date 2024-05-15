class Zoo:
    def __init__(self,fence:Fence,zookeeper:ZooKeeper):
        self.fence=fence
        self.zookeeper=zookeeper
    def describe_zoo(self):
        pass

class Fence:
    def __init__(self,area:float,temperature:float,habitat:str):
        self.area=area
        self.temperature=temperature
        self.habitat=habitat

    def area_residua(self,area:float):
        self.areaResidua=area  

         

class Animal:
    def __init__(self,name:str,species:str,age:int, height:float, width:float, preferred_habitat:str, health:float ) -> None:
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.health=health
        self.areaAnimale=height*width

    
    #def area_animale(self,height:float,width:float):
        #self.areaAnimale=height*width



class ZooKeeper:
    def __init__(self,name: str, surname:str, id:int ):
        self.name=name
        self.surname=surname
        self.id=id
    
    def add_animal(self,animal:Animal,fence:Fence):
        if 

    def remove_animal(self,animal: Animal, fence: Fence):
        pass    

    def feed(self,animal: Animal):
        pass

    def clean(self,fence: Fence):
        pass










