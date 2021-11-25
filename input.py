from nga import *
import copy


B = {
	'a': Branch('a', 3),
	'b': Branch('b', 5),
	'c': Branch('c', 2),
	'd': Branch('d', 4),
	'e': Branch('e', 3),
	'f': Branch('f', 1),
	'g': Branch('g', 4),
	'h': Branch('h', 3),
	'i': Branch('i', 3),
	'j': Branch('j', 2),
	'k': Branch('k', 5)
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
