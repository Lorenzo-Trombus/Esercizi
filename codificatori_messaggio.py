from abc import ABC, abstractmethod

class CodificatoreMessaggio:
    @abstractmethod
    def codifica(TestoinChiaro):
        return TestoinChiaro
    
class DecodificatoreMessaggio:
    def decodifica(testoCodificato):
        return testoCodificato
     