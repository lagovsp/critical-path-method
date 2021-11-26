class Node:
	__nc = 0

	def __init__(self):
		Node.__nc += 1
		self.__id = Node.__nc
		self.__ins = []
		self.__outs = []
		self.__ts = []
		self.__r = None
		self.__is_in_critical = False
		self.__is_start = None
		self.__is_end = None

	def __set_start(self, status = True):
		self.__is_start = status
		return self

	def __set_end(self, status = True):
		self.__is_end = status
		return self

	def is_end(self):
		return self.__is_end

	def is_start(self):
		return self.__is_start

	def update(self):
		if self.__is_end:
			self.__set_end()
		else:
			self.__set_end(status = False)
		if self.__is_start:
			self.__set_start()
		else:
			self.__set_start(status = False)
		return self

	def set_outs(self, es):
		self.__outs = es
		for b in self.__outs:
			b.set_from_n(self)
		self.update()
		return self

	def add_outs(self, es):
		self.__outs = self.__outs + es
		self.__outs = list(set(self.__outs))
		return self

	def set_ins(self, es):
		self.__ins = es
		for b in self.__ins:
			b.set_to_n(self)
		self.update()
		return self

	def add_ins(self, es):
		self.__ins = self.__ins + es
		self.__ins = list(set(self.__ins))
		return self

	def update_id(self, id):
		self.__id = id
		for e in self.__ins:
			e.set_to_n(self)
		for e in self.__outs:
			e.set_from_n(self)
		return self

	def merge(self, n):
		self.__outs.extend(n.__outs)
		for b in n.ins():
			b.set_to_n(self)
		for b in n.outs():
			b.set_from_n(self)
		self.update()
		return self

	def ins(self):
		return self.__ins

	def outs(self):
		return self.__outs

	def outs_ts(self):
		return [b.name() for b in self.__outs]

	def title(self):
		return self.__id

	def __str__(self):
		pl = ''
		ol = ''
		for fb in self.__ins:
			pl += f'{fb.name()}'
		for tb in self.__outs:
			ol += f'{tb.name()}'
		if not pl:
			pl = '_'
		if not ol:
			ol = '_'
		return pl + f'N{self.__id}' + ol


class Edge:
	__ec = 0

	def __init__(self, n, t):
		Edge.__ec += 1
		self.__id = Edge.__ec
		self.__n = n
		self.__t = t
		self.__from = None
		self.__to = None

	def to_n(self):
		return self.__to

	def from_n(self):
		return self.__from

	def set_to_n(self, n):
		self.__to = n
		return self

	def set_from_n(self, n):
		self.__from = n
		return self

	def time(self):
		return self.__t

	def name(self):
		return self.__n

	def __str__(self):
		if self.to_n():
			p = self.to_n().title()
		else:
			p = 'None'
		return f'{self.__t}{self.__n}B{self.from_n().title()}-{p}'


def can_merge_ns(n1, n2):
	if id(n1) == id(n2):
		return False
	if len(n1.ins()) != len(n2.ins()):
		return False
	for b in n1.ins():
		if b not in n2.ins():
			return False
	return True


def find_n_with_ins(ns, ins):
	bns = [e.name() for e in ins]
	for n in ns:
		cur_bs = [b.name() for b in n.ins()]
		if set(bns) == set(cur_bs):
			return n
	return False


def find_n_with_outs(ns, outs):
	bns = [e.name() for e in outs]
	for n in ns:
		cur_bs = [b.name() for b in n.outs()]
		if set(bns) == set(cur_bs):
			return n
	return False


def find_start_n(ns):
	return find_n_with_ins(ns, [])


def find_end_n(ns):
	return find_n_with_outs(ns, [])


def find_end_es(ns):
	ends = []
	for n in ns:
		cur_outs = n.outs()
		for eo in cur_outs:
			if not eo.to_n():
				ends.append(eo)
	return ends


def find_start_es(ns):
	starts = []
	for n in ns:
		cur_ins = n.ins()
		for ei in cur_ins:
			if not ei.from_n():
				starts.append(ei)
	return starts


def link(ins, n, outs):
	n.set_ins(ins)
	n.set_outs(outs)
	return n


class Path:
	def __init__(self):
		self.__sn = None
		self.__pl = None
		self.__t = None
		self.__p = None

	def find_critical(self):
		pass

	def set_sn(self, sn):
		self.__sn = sn

	def set_p(self, pl):
		self.__pl = pl

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
			print(f'cur leaves {cur_n.outs_ts()}')
			print(f'we go {bl}')
			if bl in cur_n.outs_ts():
				b = cur_n.outs()[cur_n.outs_ts().index(bl)]
				print()
				es.append(b.name())
				es.append(b.to_n())
				cur_n = b.to_n()
			else:
				print(es)
				print([b.name() for b in cur_n.outs()])
				raise 'path string given to Path is invalid'
		self.__p = es
		return es


class Graph:
	def update_all_id(self):
		self.__sn.update().update_id(0)
		find_end_n(self.__ns).update().update_id(len(self.__ns) - 1)
		i = 1
		for n in self.__ns:
			if not n.is_start() and not n.is_end():
				n.update().update_id(i)
				i += 1

	def __init__(self):
		self.__sn = None
		self.__ns = None
		self.__cp = None

	def complete(self):
		if not find_end_n(self.__ns):
			n = Node()
			n.set_ins(find_end_es(self.__ns))
			self.__ns.append(n)
		if not find_start_n(self.__ns):
			n = Node()
			n.set_outs(find_start_n(self.__ns))
			self.__ns.append(n)
			self.__sn = n

	def set_sn(self, sn):
		self.__sn = sn
		return self

	def set_ns(self, ns):
		self.__ns = ns
		self.__sn = find_start_n(self.__ns)

	def ns(self):
		return self.__ns

	def merge(self):
		self.complete()
		for n in self.__ns:
			def rule(test_n):
				return can_merge_ns(n, test_n)

			for n2 in list(filter(rule, self.__ns)):
				n.merge(n2)
				self.__ns.remove(n2)
		self.update_all_id()


def critical_analysis():
	pass
