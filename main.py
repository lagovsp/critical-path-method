from input import *
from sty import *
from tools import *
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network


def main():
	tutorial()
	g.organize()

	display_edges_table(g.edges(), title = 'Analysed edges', verbose = True)
	display_nodes_table(g.nodes(), title = 'Analysed nodes', verbose = True)

	show_graph(g)

	return 0


if __name__ == '__main__':
	main()
