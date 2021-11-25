class Node:
	__nc = 0
	__ns = []

	@classmethod
	def call_by_id(cls, id):
		for n in cls.__ns:
			if id == n.__id:
				return n
		return None

	def __init__(self):
		Node.__nc += 1
		self.__id = Node.__nc
		self.__in_bs = []
		self.__out_bs = []
		for b in self.__out_bs:
			b.set_left_n(self)
		Node.__ns.append(self)

	def set_out_bs(self, bs):
		self.__out_bs = bs
		for b in self.__out_bs:
			b.set_left_n(self)
		return self

	def set_in_bs(self, bs):
		self.__in_bs = bs
		for b in self.__in_bs:
			b.set_pointed_n(self)
		return self

	def merge(self, n):
		self.__out_bs.extend(n.__out_bs)
		for b in n.entering_bs():
			b.set_pointed_n(self)
		for b in n.outgoing_bs():
			b.set_left_n(self)
		return self

	def entering_bs(self):
		return self.__in_bs

	def outgoing_bs(self):
		return self.__out_bs

	def out_ts(self):
		return [b.title() for b in self.__out_bs]

	def print(self):
		print(f'Node {self.__str__()};')
		for b in self.__out_bs:
			b.print()

	def __str__(self):
		f_line = ''
		for fb in self.__in_bs:
			f_line += f'{fb.title()}'
		t_line = ''
		for tb in self.__out_bs:
			t_line += f'{tb.title()}'
		if f_line == '':
			f_line = '_'
		if t_line == '':
			t_line = '_'
		return f_line + 'N' + str(self.__id) + t_line


class Branch:
	__bc = 0
	__bs = []

	def __init__(self, title, time):
		Branch.__bc += 1
		self.__id = Branch.__bc
		self.__title = title
		self.__time = time
		self.__out_n = None
		self.__to_n = None
		Branch.__bs.append(self)

	def pointing_n(self):
		return self.__to_n

	def leaving_n(self):
		return self.__out_n

	def set_left_n(self, n):
		self.__out_n = n
		return self

	def set_pointed_n(self, n):
		self.__to_n = n
		return self

	def title(self):
		return self.__title

	def print(self):
		print(f'branch {self} leads to {self.__to_n}')

	def __eq__(self, b):
		return self.__title == b.title

	def __str__(self):
		return f'B{self.__title}{self.__time}'


def can_merge_ns(n1, n2):
	if id(n1) == id(n2):
		return False
	if len(n1.entering_bs()) != len(n2.entering_bs()):
		return False
	for b in n1.entering_bs():
		if b not in n2.entering_bs():
			return False
	return True


def find_n_w_in_bs(ns, bs):
	bns = [b.title() for b in bs]
	for n in ns:
		cur_bs = [b.title() for b in n.entering_bs()]
		if set(bns) == set(cur_bs):
			return n
	return False


def find_start_ns(ns):
	return find_n_w_in_bs(ns, [])


def find_end_bs(ns):
	next_wks = []
	for n in ns:
		next_wks.extend([b.title() for b in n.outgoing_bs()])
	next_wks = list(set(next_wks))
	start_wks = []
	for n in ns:
		start_wks.extend([b.title() for b in n.entering_bs()])
	start_wks = list(set(start_wks))
	return [it for it in next_wks if it not in start_wks]


def merge_ns(ns):
	for n in ns:
		def rule(test_n):
			return can_merge_ns(n, test_n)

		for n2 in list(filter(rule, ns)):
			n.merge(n2)
			ns.remove(n2)


def link(ibs, to_n, obs):
	return to_n.set_in_bs(ibs).set_out_bs(obs)


class Path:
	def __init__(self):
		self.__sn = None
		self.__pl = list
		self.__t = None
		self.__p = None

	def set_sn(self, sn):
		self.__sn = sn
		return self

	def set_p(self, pl):
		self.__pl = pl
		return self

	def path(self):
		if not self.__p:
			return self.__p
		else:
			return self.go_p()

	def go_p(self):
		pl = self.__pl
		es = [self.__sn]
		current_node = self.__sn
		for bl in pl:
			print()
			print(f'last node {es[len(es) - 1]}')
			print(f'cur leaves {current_node.out_ts()}')
			print(f'we go {bl}')
			if bl in current_node.out_ts():
				b = current_node.outgoing_bs()[current_node.out_ts().index(bl)]
				print()
				es.append(b.title())
				es.append(b.pointing_n())
				current_node = b.pointing_n()
			else:
				print(es)
				print([b.title() for b in current_node.outgoing_bs()])
				raise 'path string given to Path is invalid'
		self.__p = es
		return es
