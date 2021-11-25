from nga import *
from input import *
from prettytable import PrettyTable
from sty import *

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
	table.add_column(fg.orange + 'Leaving branches branches' + fg.rs, add_col)
	print(table)

	return 0


if __name__ == '__main__':
	main()
