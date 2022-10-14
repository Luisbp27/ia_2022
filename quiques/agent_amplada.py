from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        obert = [Estat(percep)]
        tancat = ()

        while obert != tancat:
            x = obert.pop()      

            if x.es_meta:

                break 
            else:
                successor = x.genera_fill
                obert.append(successor)
                tancat = tancat + successor



