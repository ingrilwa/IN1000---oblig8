""" Hovedprogrammet tester klassene node, rack, regneklynge og datasenter """

from node import Node
from rack import Rack
from regneklynge import Regneklynge
from datasenter import Datasenter

def hovedprogram():

    datasenter1 = Datasenter()
    datasenter1.lesInnRegneklynge("abel.txt")
    datasenter1.lesInnRegneklynge("saga.txt")
    datasenter1.skrivUtRegneklynge("abel.txt")



hovedprogram()
