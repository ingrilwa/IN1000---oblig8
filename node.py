""" Jeg har tatt utgangspunkt i det offentlige grensesnittet, men tatt bort og lagt til noen funksjoner i
noen av klassene. """

class Node:
    def __init__(self, minne, antPros):
        self._minne = int(minne)
        self._antPros = int(antPros)


    def antProsessorer(self):
        return self._antPros

    def noderMedNokMinne(self, paakrevdMinne):
        return self._minne >= int(paakrevdMinne)

    def hentNode(self):
        return self._minne
