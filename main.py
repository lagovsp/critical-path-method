from nga import *
from input import *
from prettytable import PrettyTable
from sty import *
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

fg.orange = Style(RgbFg(255, 150, 50))


def main():
	table = PrettyTable()
	table.title = fg.orange + 'Given branches before analyzing' + fg.rs
	table.add_column(fg.orange + 'Branch ID' + fg.rs, [b for b in B.values()])
	table.add_column(fg.orange + 'Time' + fg.rs, [b.time() for b in B.values()])
	table.add_column(fg.orange + 'From' + fg.rs, [b.leaves() for b in B.values()])
	table.add_column(fg.orange + 'To' + fg.rs, [b.points() for b in B.values()])
	print(table)

	merge_ns(N)

	table = PrettyTable()
	table.title = fg.orange + 'After analysis' + fg.rs
	table.add_column(fg.orange + 'Branch ID' + fg.rs, [b for b in B.values()])
	table.add_column(fg.orange + 'Time' + fg.rs, [b.time() for b in B.values()])
	table.add_column(fg.orange + 'From' + fg.rs, [b.leaves() for b in B.values()])
	table.add_column(fg.orange + 'To' + fg.rs, [b.points() for b in B.values()])
	add_col = [[i.__str__() for i in b.leaves().entered_bs()] for b in B.values()]
	table.add_column(fg.orange + 'Prev branches' + fg.rs, add_col)
	print(table)

	table = PrettyTable()
	table.title = fg.orange + 'Nodes after analysis' + fg.rs
	table.add_column(fg.orange + 'Node ID' + fg.rs, N)
	add_col = [[i.__str__() for i in b.entered_bs()] for b in N]
	table.add_column(fg.orange + 'Entering branches' + fg.rs, add_col)
	add_col = [[i.__str__() for i in b.out_bs()] for b in N]
	table.add_column(fg.orange + 'Leaving branches' + fg.rs, add_col)
	print(table)

	print(find_end_bs(N))
	last_node = Node()
	last_node.set_entering_bs([B[l] for l in find_end_bs(N)])
	print([b.__str__() for b in last_node.entered_bs()])
	print(last_node)
	print([b.__str__() for b in last_node.out_bs()])

	G = nx.DiGraph()

	l = []
	for b in B.values():
		l.append((f'{b.leaves().title()}', f'{b.points().title()}'))
	print(l)

	G.add_edges_from(
		l)  # grani

	val_map = {'A': 0,
	           'D': 0,
	           'H': 0}

	values = [val_map.get(node, 0.25) for node in G.nodes()]

	# Specify the edges you want here
	# red_edges = [('A', 'C'), ('E', 'C')]
	# edge_colours = ['black' if not edge in red_edges else 'red'
	#                 for edge in G.edges()]
	# black_edges = [edge for edge in G.edges() if edge not in red_edges]
	#
	# pos = nx.spring_layout(G)
	# nx.draw_networkx_nodes(G, pos, cmap = plt.get_cmap('jet'), node_color = values, node_size = 500)
	# nx.draw_networkx_labels(G, pos)
	# nx.draw_networkx_edges(G, pos, edgelist = red_edges, edge_color = 'r', arrows = True)
	# nx.draw_networkx_edges(G, pos, edgelist = black_edges, arrows = True)
	print(G)
	net = Network()
	net.from_nx(G)
	net.show('g.html')

	return 0


if __name__ == '__main__':
	main()
