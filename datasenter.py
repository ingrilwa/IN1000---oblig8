""" Jeg har tatt utgangspunkt i det offentlige grensesnittet, men tatt bort og lagt til noen funksjoner i
noen av klassene. """

from regneklynge import Regneklynge
from node import Node
class Datasenter:

    def __init__(self):
        self._ordbok = {}

    def lesInnRegneklynge(self, filnavn):
        for linje in open(filnavn):
           data = linje.strip().split(" ")
           antallNoder = data[0]
           if len(data) == 1:
               self._ordbok[filnavn] = Regneklynge(data[0])
           else:
               antallNoder = data[0]
               minnePerNode = data[1]
               antProsPerNode = data[2]
               for e in range(int(antallNoder)):
                   self._ordbok[filnavn].settInn(Node(minnePerNode, antProsPerNode))

    def skrivUtRegneklynge(self, filnavn):
        for data in self._ordbok.values():
            print("Informasjon om regneklyngen", filnavn)
            print("Antall racks", data.antRacks())
            print("Antall prosessorer", data.antProsessorer())
            print("Noder med minst 32 GB", data.noderMedNokMinne(32))
            print("Noder med minst 64 GB", data.noderMedNokMinne(64))
            print("Noder med minst 128 GB", data.noderMedNokMinne(128))


    def skrivUtAlleRegneklynger(self):
        for verdi in self._ordbok:
            return self.skrivUtRegneklynge(verdi)
