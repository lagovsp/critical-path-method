from input import *
from tools import *


def main():
	tutorial()
	g.organize()

	display_edges_table(g.edges(), title = 'Analysed edges', verbose = True)
	display_nodes_table(g.nodes(), title = 'Analysed nodes', verbose = True)
	show_graph(g)

	return 0


if __name__ == '__main__':
	main()
