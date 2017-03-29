# Reading a scheme expression

# lexical analysis 
# first send each line to the tokenizer
# iterative process 
# checks for malformed tokens
# Determines types of tokens # for ex, 23 is one item, ( is another. 
# reads one line at a time

# syntactic analysis
# Tree-recursive process
# Balances paranthesis 
# Returns tree structure
# Processes multiple lines at once

# Parser which we're building
# predictive recursive descent parser
# inspects k tokens to decide what structure to build


# It makes a lot of sense to me why syntactic analysis is a 
# recursive process.

# Let's consider an example 
# So, our lexical analysis
# returns an object which is basically a list which holds something like
# '(', '+', 1, '(', '-', 23, ')', '(', '*', 4, 5.6, ')', ')' 

# Okay, so lets perform syntactic analysis on the sequence shown above.
# we have a function called scheme_read into which we pass our tokens. 
# Base case - any symbol or number
# So, if not the base case then we probably just hit a bracket aka a sub expression
# So, we just call scheme_read on the sub expression; 
# An elegant mutually recursive process was used in the lecture'

# I'll write down the implementation shown in the lecture here
# so that I can understand it better
# A lot of the objects haven't been defined so
# this functions isn't going to work
# think of it as pseudo code instead of actual code

def scheme_read(src):
	# note that src is not a list. It is 
	# a user defined object

	if src.current() is None:
		raise EOFError

	val = src.pop() # gets the first element
	if val == 'nil': # first base case
		return nil # an object which is defined
	elif val not in DELIMITERS: # ( . # '
		return val
	elif val == '(': # started our first expression
		return read_tail(src) 
	else:
		raise SyntaxError("Unexpected token {0}".format(val))


def read_tail(src):
	if src.current() is None:
		raise SyntaxError("Unexpected end of file") # we just encountered '('
	elif src.current() == ')':
		src.pop()
		return nil
	first = scheme_read(src) # reads the first item, whatever it is expression symbol number etc
	second = read_tail(src) # reads the rest of the items

	return Pair(first, second)

# So, how does this work. 
# the base cases for scheme_read are self explanatory so I'll be skipping them

# In the scheme_read function, if we hit the else case
# then we've clearly encountered an unknown token
# so, we raise a SyntaxError
# if val == '(', then we've hit the beginning of an expression
# so we call read_tail on src

# Now read_tail is a really cool function
# The first base case should be clear,
# we just opened a bracket. If we hit the end w/o closing it then that's an error
# if we close the bracket then the expression is just ()

# Now the rest of read_tail does a lot of interesting work
# we call scheme_read on the first item in src
# so it reads in whatever the first item was, a number an expression a symbol
# Now we need to look for the closing ')', so we just call read_tail on the rest
# note that src is modified with every call of scheme_read

# Then we just just return a Pair with all the information encoded
# A pair is just used to represent scheme lists
# Also scheme expressions are represented as scheme lists
# Source code is data
# And now we've completed the complicated yet elegant syntactic analysis. Wohoo!





# Evaluating a scheme expression (or the Pair object which we just created)

# okay so let's understand how the basic evaluation happens
# Let's start with an example
# (* 3 (+ 1 2) (* 1 3))
# so we just call scheme_read on this which returns a pair
# Pair(*, Pair(Pair(+, Pair(1, Pair(2, nil))), Pair(*, Pair(1, Pair(3, nil))))

# If it were a tree it would look something like this
# *
# 	3
#	+
#		1
#		2
#	*
#		1
#		3

# Okay, so we can clearly evaluate this recursively
# How?
# well we see what the first element of the pair is
# if it is a +
# then we add all the other elements in the sequence
# if it is a *
# then we just multiple all the other elements in the sequence
# if it is a -
# if there is only one argument
# we return the negative of that
# else we return sub(first, rest)
# if it is a /
# we return / first, rest, recursively of course
# if it is a number, hey, base case!
# return the number


# for the initial calculator interpreter we're building
# we're going to write the eval/apply functions now
# the expression which gets evaluated is always a number
# again consider the following code as pseudo code since we haven't 
# implemented a lot of the required objects yet

def calc_eval(exp):
	if type(exp) in (int, float):
		return exp 
	elif isinstance(exp, Pair):
		argument = exp.second.map(calc_eval)
		return calc_apply(exp.first, arguments)
	else:
		raise TypeError(exp + ' is not a number or call expression')

def calc_apply(operator, args):
	if not isinstance(operator, str):
		raise TypeError(str(operator) + ' is not a symbol')

	if operator == '+':
		return reduce(add, args, 0)
	elif operator == '*':
		return reduce(mul, args, 1)
	elif operator == '-':
		if len(args) == 0:
			raise TypeError('- requires at least one argument')
		elif len(args) == 1:
			return -args.first
		else:
			return reduce(sub, args.second, args.first)
	elif operator == '/':
		if len(args) == 0:
			raise TypeError('- requires at least one argument')
		elif len(args) == 1:
			return 1 / args.first
		else:
			return reduce(truediv, args.second, args.first)
	else:
		return operator + ' is an unknown operator'



# REPL

# a prompt telling the user to type something
# Read text input from the user 
# Parse text into an expression
# evaluate the expression
# if error
# print error
# else
# print result

def read_eval_print_loop():
	while True:
		try:
			src = buffer_input() # does the lexical analysis
			while src.more_on_line:
				expression = scheme_read(src) # returns the scheme list
				print (calc_eval(expression))
		except (SyntaxError, ValueError, TypeError, ZeroDivisionError) as e:
			print (type(e).__name__ + ':' + e) 
		except (KeyboardInterrup, EOFError) as e:
			print ('calculation completed')
			return 

























