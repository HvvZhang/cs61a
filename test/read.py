class nil:
	"""Represents an empty pair in scheme"""
	def __repr__(self):
		return 'nil'

	def __len__(self):
		return 0

	def __getitem__(self, i):
		raise IndexError("Index out of range")

	def map(self, fn):
		return nil

nil = nil() # there should only every be one instance of this

class Pair:
	"""Represents the built in Pair datastructure in scheme"""
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __repr__(self):
		return 'Pair({0}, {1})'.format(repr(self.first), repr(self.second))

	def __len__(self):
		return 1 + len(self.second)


	# the base cases for the following two functions are defined by 
	# nil object
	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.second[i - 1]

	def map(self, fn):
		return Pair(fn(self.first), self.second.map(fn))


def eval_and(operands):
	filtered_oprands = [False if x is False else True for x in operands]
	return all(operands)


