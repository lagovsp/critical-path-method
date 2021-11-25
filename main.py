from nga import *
from input import *
import copy


def main():
	for n in N:
		print(n)
	# for n1 in N:
	# 	for n2 in N:
	# 		if can_merge_ns(n1, n2):
	# 			n1.merge(n2)
	# 			N.remove(n2)

	merge_ns(N)

	print()
	for n in N:
		print(n)
	# print()
	# print()
	#
	# for n in N:
	# 	# print(n)
	# 	n.print()
	# new = copy.deepcopy(N)
	# new_order = []
	# while True:
	# 	for n in new_order:
	# 		if not n.in_bs():
	# 			new_order.append(n)
	# 			new.remove(n)

	sn = find_start_ns(N)
	print(f'sn - {sn}')
	p = Path()
	p.set_sn(sn)
	p.set_p(['a', 'c', 'e'])
	a = p.go_p()
	for it in a:
		print(it.__str__())
	return 0


if __name__ == '__main__':
	main()
