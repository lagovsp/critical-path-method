from nga import *
from input import *
from sty import *
from tools import display_edges_table, display_nodes_table, tutorial
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

fg.orange = Style(RgbFg(255, 150, 50))


def main():
	tutorial()
	
	g.organize()
	g.calculate_parameters()

	display_edges_table(g.es(), title = 'Edges after analysis', verbose = True)
	display_nodes_table(g.ns(), title = 'Nodes after analysis', verbose = True)

	return 0


if __name__ == '__main__':
	main()
