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
	table.title = fg.orange + 'Given edges before analyzing' + fg.rs
	table.add_column(fg.orange + 'Edge ID' + fg.rs, [b for b in B.values()])
	table.add_column(fg.orange + 'Time' + fg.rs, [b.time() for b in B.values()])
	table.add_column(fg.orange + 'From' + fg.rs, [b.from_n() for b in B.values()])
	table.add_column(fg.orange + 'To' + fg.rs, [b.to_n() for b in B.values()])
	print(table)

	# Node.set_ns(N)
	# Node.merge_ns()

	g.merge()

	table = PrettyTable()
	table.title = fg.orange + 'Edges after analysis' + fg.rs
	table.add_column(fg.orange + 'Edge ID' + fg.rs, [b for b in B.values()])
	table.add_column(fg.orange + 'Time' + fg.rs, [b.time() for b in B.values()])
	table.add_column(fg.orange + 'From' + fg.rs, [b.from_n() for b in B.values()])
	table.add_column(fg.orange + 'To' + fg.rs, [b.to_n() for b in B.values()])
	add_col = [[i.__str__() for i in b.from_n().ins()] for b in B.values()]
	table.add_column(fg.orange + 'Prev branches' + fg.rs, add_col)
	print(table)

	table = PrettyTable()
	table.title = fg.orange + 'Nodes after analysis' + fg.rs
	table.add_column(fg.orange + 'Node ID' + fg.rs, N)
	add_col = [[i.__str__() for i in b.ins()] for b in N]
	table.add_column(fg.orange + 'Entering branches' + fg.rs, add_col)
	add_col = [[i.__str__() for i in b.outs()] for b in N]
	table.add_column(fg.orange + 'Leaving branches' + fg.rs, add_col)
	print(table)

	return 0


if __name__ == '__main__':
	main()
