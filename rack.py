""" Jeg har tatt utgangspunkt i det offentlige grensesnittet, men tatt bort og lagt til noen funksjoner i
noen av klassene. """
from node import Node
class Rack:

    def __init__(self):
        self._nodeliste = []

    ## Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
         self._nodeliste.append(node)

    ## Henter antall noder i racket
    # @return antall noder
    def getAntNoder(self):
        return len(self._nodeliste)

    ## Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def antProsessorer(self):
        teller = 0
        for node in self._nodeliste:
            teller += node.antProsessorer()
        return teller

    ## Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        teller = 0
        for node in self._nodeliste:
            if node.noderMedNokMinne(paakrevdMinne):
                teller += 1
        return teller
