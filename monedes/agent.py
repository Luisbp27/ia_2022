""" Mòdul que conté l'agent per jugar al joc de les monedes.

Percepcions:
    ClauPercepcio.MONEDES
Solució:
    " XXXC"
"""

from aspirador.entorn import ClauPercepcio
from ia_2022 import agent, entorn
import queue

SOLUCIO = " XXXC"

class Estat:
    # estats = [0, 0, 0, 0, 2] hasta [1, 1, 1, 1, 2]
    pass

class AgentMoneda(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=0)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def pinta(self, display):
        print(self._posicio_pintar)

    def _cerca(self, estat):
        self.__oberts = queue.PriorityQueue()
        self.__tancats = set()

        self.__oberts.put(estat)
        actual = None
        while len(self.__oberts) > 0:
            actual = self.get()

            if actual in self.__tancats:
                continue

            if not actual.es_segur():
                self.__tancats.add(actual)
                continue

            estats_fills = actual.genera_fill()

            if actual.es_meta():
                break

            for estat_f in estats_fills:
                self.__oberts.put(estat_f)

            self.__tancats.add(actual)

        if actual is None:
            raise ValueError("Error impossible")

        if actual.es_meta():
            accions = []
            iterador = actual

            while iterador.pare is not None:
                pare, accio = iterador.pare

                accions.append(accio)
                iterador = pare

            self.__accions = accions
            return True

    def claculate_f(self, estat):
        pass

    def actua(
        self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        pass
        
