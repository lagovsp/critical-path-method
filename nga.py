class Node:
	__node_counter = 0

	def __init__(self, next_b):
		Node.__node_counter += 1
		self.__id = Node.__node_counter
		self.__prev_bs = []
		self.__next_bs = [next_b]
		for b in self.__next_bs:
			b.set_prev_n(self)

	def set_from_branches(self, branches):
		self.__prev_bs = branches
		for branch in self.__prev_bs:
			branch.set_next_n(self)
		return self

	def merge(self, branch):
		self.__next_bs.extend(branch.__next_bs)
		return self

	def prev_bs(self):
		return self.__prev_bs

	def __str__(self):
		f_line = ''
		for fb in self.__prev_bs:
			f_line += f'{fb.name()}'
		t_line = ''
		for tb in self.__next_bs:
			t_line += f'{tb.name()}'
		if f_line == '':
			f_line = '_'
		if t_line == '':
			t_line = '_'
		return f_line + 'N' + str(self.__id) + t_line


class Branch:
	__branch_counter = 0

	def __init__(self, name, time):
		Branch.__branch_counter += 1
		self.__id = Branch.__branch_counter
		self.__name = name
		self.__time = time
		self.__from_node = None
		self.__to_node = None

	def set_prev_n(self, node):
		self.__from_node = node
		return self

	def set_next_n(self, node):
		self.__to_node = node
		return self

	def name(self):
		return self.__name

	def __eq__(self, b):
		return self.__name == b.name

	def __str__(self):
		return f'B{self.__name}{self.__time}'


def can_merge_ns(n1, n2):
	if id(n1) == id(n2):
		return False
	if len(n1.prev_bs()) != len(n2.prev_bs()):
		return False
	for b in n1.prev_bs():
		if b not in n2.prev_bs():
			return False
	return True


def link(branches, to_node):
	to_node.set_from_branches(branches)
	return to_node
