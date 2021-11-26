from nga import *

B = {
	'a': Edge('a', 3),
	'b': Edge('b', 5),
	'c': Edge('c', 2),
	'd': Edge('d', 4),
	'e': Edge('e', 3),
	'f': Edge('f', 1),
	'g': Edge('g', 4),
	'h': Edge('h', 3),
	'i': Edge('i', 3),
	'j': Edge('j', 2),
	'k': Edge('k', 5)
}

N = [
	link([], Node(), [B['a']]),
	link([], Node(), [B['b']]),
	link([(B['a'])], Node(), [B['c']]),
	link([], Node(), [B['d']]),
	link([B['b'], B['c']], Node(), [B['e']]),
	link([B['a']], Node(), [B['f']]),
	link([B['b'], B['c']], Node(), [B['g']]),
	link([B['a']], Node(), [B['h']]),
	link([B['h'], B['g']], Node(), [B['i']]),
	link([B['f'], B['e'], B['d']], Node(), [B['j']]),
	link([B['b'], B['c']], Node(), [B['k']])
]

g = Graph()
g.set_ns(N)
