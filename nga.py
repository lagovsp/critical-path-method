class Node:
	__nc = 0

	def __init__(self):
		Node.__nc += 1
		self.__id = Node.__nc
		self.__entered_bs = []
		self.__out_bs = []
		for b in self.__out_bs:
			b.set_left_n(self)

	def set_outgoing_bs(self, bs):
		self.__out_bs = bs
		for b in self.__out_bs:
			b.set_left_n(self)
		return self

	def set_entering_bs(self, bs):
		self.__entered_bs = bs
		for b in self.__entered_bs:
			b.set_pointed_n(self)
		return self

	def merge(self, n):
		self.__out_bs.extend(n.__out_bs)
		for b in n.entered_bs():
			b.set_pointed_n(self)
		for b in n.out_bs():
			b.set_left_n(self)
		return self

	def entered_bs(self):
		return self.__entered_bs

	def out_bs(self):
		return self.__out_bs

	def out_ts(self):
		return [b.title() for b in self.__out_bs]

	def title(self):
		return self.__id

	def __str__(self):
		pl = ''
		ol = ''
		for fb in self.__entered_bs:
			pl += f'{fb.title()}'
		for tb in self.__out_bs:
			ol += f'{tb.title()}'
		if not pl:
			pl = '_'
		if not ol:
			ol = '_'
		return pl + f'N{self.__id}' + ol


class Branch:
	__bc = 0
	# __bs = []

	def __init__(self, title, time):
		Branch.__bc += 1
		self.__id = Branch.__bc
		self.__title = title
		self.__time = time
		self.__left_n = None
		self.__pointed_n = None
	# Branch.__bs.append(self)

	def points(self):
		return self.__pointed_n

	def leaves(self):
		return self.__left_n

	def set_pointed_n(self, n):
		self.__pointed_n = n
		return self

	def set_left_n(self, n):
		self.__left_n = n
		return self

	def time(self):
		return self.__time

	def title(self):
		return self.__title

	def __str__(self):
		if self.points():
			p = self.points().title()
		else:
			p = 'None'
		return f'{self.__time}{self.__title}B{self.leaves().title()}-{p}'


def can_merge_ns(n1, n2):
	if id(n1) == id(n2):
		return False
	if len(n1.entered_bs()) != len(n2.entered_bs()):
		return False
	for b in n1.entered_bs():
		if b not in n2.entered_bs():
			return False
	return True


def find_n_w_in_bs(ns, bs):
	bns = [b.title() for b in bs]
	for n in ns:
		cur_bs = [b.title() for b in n.entered_bs()]
		if set(bns) == set(cur_bs):
			return n
	return False


def find_start_ns(ns):
	return find_n_w_in_bs(ns, [])


def find_end_bs(ns):
	next_wks = []
	for n in ns:
		next_wks.extend([b.title() for b in n.out_bs()])
	next_wks = list(set(next_wks))
	start_wks = []
	for n in ns:
		start_wks.extend([b.title() for b in n.entered_bs()])
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
	return to_n.set_entering_bs(ibs).set_outgoing_bs(obs)


class Path:
	def __init__(self):
		self.__sn = None
		self.__pl = None
		self.__t = None
		self.__p = None

	def set_sn(self, sn):
		self.__sn = sn
		return self

	def set_p(self, pl):
		self.__pl = pl
		return self

	def path(self):
		if self.__p:
			return self.__p
		else:
			return self.go_p()

	def go_p(self):
		pl = self.__pl
		es = [self.__sn]
		cur_n = self.__sn
		for bl in pl:
			print()
			print(f'last node {es[len(es) - 1]}')
			print(f'cur leaves {cur_n.out_ts()}')
			print(f'we go {bl}')
			if bl in cur_n.out_ts():
				b = cur_n.out_bs()[cur_n.out_ts().index(bl)]
				print()
				es.append(b.title())
				es.append(b.points())
				cur_n = b.points()
			else:
				print(es)
				print([b.title() for b in cur_n.out_bs()])
				raise 'path string given to Path is invalid'
		self.__p = es
		return es
