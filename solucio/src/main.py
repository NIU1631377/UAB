##########################################################################
#########            Funció main del seminari 3 de MD           ##########
#########              Copyright 2022 Bernat Gastón             ##########
#########               Author: Bernat Gastón                   ##########
#########            Contact: bernat.gaston@uab.cat             ##########
#########   Alumnes:                                            ##########
##########################################################################

from graph import Node, Graph
from cerques import BFS, DFS

'''
Funció que crea un graf simulant una mini internet
@return: el graf creat
'''
def crea_internet():
    #CREAR NODES
    JocsiEsport = Node('JocsiEsport', 0, 0)
    TotJocs = Node('TotJocs', 2, 0)
    SPORT = Node('SPORT', -2, 0)
    MARCA = Node('MARCA', 0, 2)
    AS = Node('AS', 0, -2)
    NBATotal = Node('NBATotal', 2, 2)
    LOLFans = Node('LOLFans', 2, -2)
    AmongUsEurope =Node('AmongUsEurope', -2, 2)
    LOLCommunity =Node('LOLCommunity', -2, -2)

    #CREAR GRAPH I AFEGIR NODES
    internet = Graph(True)
    internet.add_node(JocsiEsport)
    internet.add_node(TotJocs)
    internet.add_node(SPORT)
    internet.add_node(MARCA)
    internet.add_node(NBATotal)
    internet.add_node(AS)
    internet.add_node(LOLFans)
    internet.add_node(LOLCommunity)
    internet.add_node(AmongUsEurope)

    #AFEGIR ARESTES
    internet.add_edge(JocsiEsport, TotJocs)
    internet.add_edge(JocsiEsport, SPORT)
    internet.add_edge(JocsiEsport, MARCA)
    internet.add_edge(JocsiEsport, AS)

    internet.add_edge(SPORT, NBATotal)
    internet.add_edge(AS, NBATotal)

    internet.add_edge(TotJocs, LOLFans)
    internet.add_edge(TotJocs, AmongUsEurope)

    internet.add_edge(AmongUsEurope, LOLFans)

    internet.add_edge(LOLFans, AmongUsEurope)
    internet.add_edge(LOLFans, LOLCommunity)

    internet.add_edge(LOLCommunity, JocsiEsport)
    internet.draw()
    return internet


if __name__ == '__main__':
    internet = crea_internet()
