""" Jeg har tatt utgangspunkt i det offentlige grensesnittet, men tatt bort og lagt til noen funksjoner i
noen av klassene. """

from node import Node
from rack import Rack
class Regneklynge:
    ## Oppretter en regneklynge og setter maks antall
    # det er plass til i et rack
    # @param noderPerRack max antall noder per rack
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._regneklynge = []

         # Sjekker om det er plass til flere noder i racket

    def settInn(self, node):
        if len(self._regneklynge) < 1:
            rack1 = Rack()
            self._regneklynge.append(rack1)
            rack1.settInn(node)
        else:
            for e in self._regneklynge:
                if e.getAntNoder() > int(self._noderPerRack):
                    e.settInn(node)
                    return 

            nyRack = Rack()
            nyRack.settInn(node)
            self._regneklynge.append(nyRack)


    ## Beregner totalt antall prosessorer i hele regneklyngen
    # @return totalt antall prosessorer
    def antProsessorer(self):
        teller = 0
        for e in self._regneklynge:
            teller += e.antProsessorer()
        return teller

    ## Beregner antall noder i regneklyngen med minne over angitt grense
    # @param paakrevdMinne hvor mye minne skal noder som telles med ha
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        teller = 0
        for e in self._regneklynge:
            if e.noderMedNokMinne(paakrevdMinne):
                teller += 1
        return teller

    ## Henter antall racks i regneklyngen
    # @return antall racks
    def antRacks(self):
        return len(self._regneklynge)
