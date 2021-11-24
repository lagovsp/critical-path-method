from nga import *
from input import *


def main():
	for n in N:
		print(n)

	for b in B.values():
		print(b)

	print('nodes old\n')
	for n in N:
		print(n)

	for n1 in N:
		for n2 in N:
			if can_merge_ns(n1, n2):
				n1.merge(n2)
				N.remove(n2)

	print('nodes new\n')
	for n in N:
		print(n)

	return 0


if __name__ == '__main__':
	main()
