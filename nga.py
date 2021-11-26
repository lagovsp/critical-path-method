class Node:
	__nc = 0

	@staticmethod
	def can_merge_ns(n1, n2):
		if id(n1) == id(n2):
			return False
		if len(n1.ins()) != len(n2.ins()):
			return False
		for b in n1.ins():
			if b not in n2.ins():
				return False
		return True

	def __init__(self):
		Node.__nc += 1
		self.__id = Node.__nc
		self.__ins = []
		self.__outs = []
		self.__t_e_l_r = [None, None, None]
		self.__is_in_critical = False
		self.__is_start = None
		self.__is_end = None

	def check_if_is_start(self):
		if not self.__ins:
			self.__is_start = True
		else:
			self.__is_start = False
		return self

	def check_if_is_end(self):
		if not self.__outs:
			self.__is_end = True
		else:
			self.__is_end = False
		return self

	def is_end(self):
		return self.__is_end

	def is_start(self):
		return self.__is_start

	def is_in_critical(self):
		return self.__is_in_critical

	def update(self):
		self.check_if_is_start()
		self.check_if_is_end()
		return self

	def set_outs(self, es):
		self.__outs = es
		for b in self.__outs:
			b.set_from_n(self)
		self.update()
		return self

	# def add_outs(self, es):
	# 	self.__outs = self.__outs + es
	# 	self.__outs = list(set(self.__outs))
	# 	return self

	def set_ins(self, es):
		self.__ins = es
		for b in self.__ins:
			b.set_to_n(self)
		self.update()
		return self

	# def add_ins(self, es):
	# 	self.__ins = self.__ins + es
	# 	self.__ins = list(set(self.__ins))
	# 	return self

	def update_id(self, id):
		self.__id = id
		for e in self.__ins:
			e.set_to_n(self)
		for e in self.__outs:
			e.set_from_n(self)
		return self

	def calculate_te(self):
		self.__t_e_l_r[0] = max([ei.from_n().calculate_te() + ei.time() for ei in self.__ins], default = 0)
		return self.__t_e_l_r[0]

	def calculate_tl(self):
		self.__t_e_l_r[1] = min([eo.to_n().calculate_tl() - eo.time() for eo in self.__outs], default =
		self.__t_e_l_r[0])
		return self.__t_e_l_r[1]

	def calculate_r(self):
		self.__t_e_l_r[2] = self.__t_e_l_r[1] - self.__t_e_l_r[0]
		if self.__t_e_l_r[2] == 0:
			self.__is_in_critical = True
		if self.__t_e_l_r[2] == 0:
			self.__is_in_critical = True
		return self.__t_e_l_r[2]

	def merge(self, n):
		for e in n.outs():
			if e not in self.__outs:
				self.__outs.append(e)
		# self.__outs.extend(n.__outs)
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

	def times(self):
		return self.__t_e_l_r

	def name(self):
		return self.__id

	def __str__(self):
		pl, ol = '', ''
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
		self.__t_ls = None
		self.__t_ee = None
		self.__r_fl_fr = [None, None]
		self.__from = None
		self.__to = None
		self.__is_in_critical = False

	def calculate(self):
		self.__t_ls = self.__to.times()[1] - self.__t
		self.__t_ee = self.__from.times()[0] + self.__t
		self.__r_fl_fr[0] = self.__to.times()[1] - self.__from.times()[0] - self.__t
		self.__r_fl_fr[1] = self.__to.times()[0] - self.__from.times()[0] - self.__t

	def check_if_is_in_critical(self):
		if self.__from.is_in_critical() and self.__to.is_in_critical():
			self.__is_in_critical = True
		else:
			self.__is_in_critical = False

	def is_in_critical(self):
		return self.__is_in_critical

	def tls_tee_rfl_rfr(self):
		return [self.__t_ls, self.__t_ee, self.__r_fl_fr[0], self.__r_fl_fr[1]]

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
			t = self.to_n().name()
		else:
			t = 'None'
		if self.from_n():
			f = self.from_n().name()
		else:
			f = 'None'
		return f'{self.__t}{self.__n}E{f}-{t}'


def find_n_with(nodes, edges, flag = 'ins'):
	ens = [e.name() for e in edges]
	for n in nodes:
		cur_bs = [b.name() for b in n.ins()]
		if flag == 'outs':
			cur_bs = [b.name() for b in n.outs()]
		if set(ens) == set(cur_bs):
			return n
	return False


# def find_n_with_outs(ns, outs):
# 	bns = [e.name() for e in outs]
# 	for n in ns:
# 		cur_bs = [b.name() for b in n.outs()]
# 		if set(bns) == set(cur_bs):
# 			return n
# 	return False


def find_start(ns):
	return find_n_with(ns, [], flag = 'ins')


def find_end(ns):
	return find_n_with(ns, [], flag = 'outs')


def find_endless_edges(ns):
	ends = []
	for n in ns:
		cur_outs = n.outs()
		for eo in cur_outs:
			if not eo.to_n():
				ends.append(eo)
	return ends


def find_startless_edges(ns):
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


# class Path:
# 	def __init__(self):
# 		self.__sn = None
# 		self.__pl = None
# 		self.__t = None
# 		self.__p = None
#
# 	def find_critical(self):
# 		pass
#
# 	def set_sn(self, sn):
# 		self.__sn = sn
#
# 	def set_p(self, pl):
# 		self.__pl = pl
#
# 	def path(self):
# 		if self.__p:
# 			return self.__p
# 		else:
# 			return self.go_p()
#
# 	def go_p(self):
# 		pl = self.__pl
# 		es = [self.__sn]
# 		cur_n = self.__sn
# 		for bl in pl:
# 			print()
# 			print(f'last node {es[len(es) - 1]}')
# 			print(f'cur leaves {cur_n.outs_ts()}')
# 			print(f'we go {bl}')
# 			if bl in cur_n.outs_ts():
# 				b = cur_n.outs()[cur_n.outs_ts().index(bl)]
# 				print()
# 				es.append(b.name())
# 				es.append(b.to_n())
# 				cur_n = b.to_n()
# 			else:
# 				print(es)
# 				print([b.name() for b in cur_n.outs()])
# 				raise 'path string given to Path is invalid'
# 		self.__p = es
# 		return es


class Graph:
	def __init__(self):
		self.__sn = None
		self.__ns = None
		self.__cpt = None

	def update_all_id(self):
		self.__sn.update().update_id(1)
		find_end(self.__ns).update().update_id(len(self.__ns))
		i = 2
		for n in self.__ns:
			n.update()
			if not n.is_start() and not n.is_end():
				n.update_id(i)
				i += 1

	def complete(self):
		if not find_end(self.__ns):
			n = Node()
			n.set_ins(find_endless_edges(self.__ns))
			self.__ns.append(n)
		if not find_start(self.__ns):
			n = Node()
			n.set_outs(find_start(self.__ns))
			self.__ns.append(n)
			self.__sn = n

	def cpt(self):
		return self.__cpt

	def nodes(self):
		return self.__ns

	def edges(self):
		pushed = []
		result = []
		for n in self.__ns:
			for e in n.ins():
				if not id(e) in pushed:
					result.append(e)
					pushed.append(id(e))
			for e in n.outs():
				if not id(e) in pushed:
					result.append(e)
					pushed.append(id(e))
		return result

	# def set_sn(self, sn):
	# 	self.__sn = sn
	# 	return self

	def set_nodes(self, ns):
		self.__ns = ns
		self.__sn = find_start(self.__ns)

	def merge(self):
		for n in self.__ns:
			def rule(test_n):
				return Node.can_merge_ns(n, test_n)

			for n2 in list(filter(rule, self.__ns)):
				n.merge(n2)
				self.__ns.remove(n2)

	def calculate_parameters(self):
		find_end(self.__ns).calculate_te()
		find_start(self.__ns).calculate_tl()
		for n in self.__ns:
			n.calculate_r()
		for e in self.edges():
			e.calculate()

	def pave_way(self):
		# cur_node = self.__sn
		# while cur_node.outs():
		# 	for eo in cur_node.outs():
		# 		if eo.to_n().times()[2] == 0:
		# 			eo.check_if_is_in_critical()
		# 			cur_node = eo.to_n()
		# 			break
		self.__cpt = 0
		cur_node = find_end(self.__ns)
		while cur_node.ins():
			for ei in cur_node.ins():
				if ei.from_n().times()[2] == 0:
					ei.check_if_is_in_critical()
					self.__cpt += ei.time()
					cur_node = ei.from_n()
					break

	def organize(self):
		self.merge()
		self.complete()
		self.update_all_id()
		self.calculate_parameters()
		self.pave_way()
