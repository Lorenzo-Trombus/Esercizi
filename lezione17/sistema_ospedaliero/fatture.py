from paziente import Paziente
from dottore import Dottore



class Fattura:
    
    def __init__(self,patient:list[Paziente], doctor:Dottore) -> None:
        self.patient=[]
        self.doctor=Dottore
        
        
        if doctor.isAValidDoctor()== f"Doctor {doctor.first_name} {doctor.last_name} is valid":
            self.fatture:int=len(patient)
            self.salary:int=0
        else:
            self.patient=None
            self.doctor=None
            self.fatture=None
            self.salary=None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")


    def getSalary(self):
        self.salary=self.doctor.getParcel()*self.fatture
        