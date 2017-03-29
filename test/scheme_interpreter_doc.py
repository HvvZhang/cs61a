# Eval and apply functions

# eval function
# Base case - primitive values such as numbers, values bound to symbols. 
# Recursive call - 
# As soon as we find an expression
# apply procedure to arguments
# or handle special forms such as if, 
# by calling eval on sub expressions inside the if.
# Note that eval will need an environment to look up symbols

# symbols are bound to values in the current environment
# self evaluating expressions are returned, for ex - numbers/empty list
# all other expressions are scheme lists called combinations

# the if special form
# (if (exp1) (exp2) (exp3))
# for the if expression, we evaluate the predicate,
# and based on that we decide which of expr2 or exp3 to evaluate

# quote special form
# (quote (a b c)) just evaluates to the scheme list (a b c) a b c are not evaluated
# (quote (a b)) can also be written as '(a b)
# the scheme_read function should convert '(a b) to just (quote (a b))

# the lambda special form
# (lambda (<formal parameters>) (<body>))

class LambdaProcedure:
	def __init__(self, formals, body, env):
		self.formals = formals
		self.body = body
		self.env = env

# formals is a scheme list of symbols
# body is a scheme expression
# env is the environment where the procedure was defined

# the define special form
# binds a symbol to a value in the first frame of the current environment
# (define <name> <expression>)
# first, we evaluate the expression
# then, in the current frame, we bind <name> to the value of the <expression>

# define behaves a bit differently for procedures
# (define (<name> <formal parameters>) (<body>))
# is converted to (define <name> (lambda (<formal parameters>) (<body>)))
#=========================================

# apply function
# Base case - built in primitive procedure
# If we encounter a user defined procedure
# call eval on the body of the procedure which is also an expression
# whenever eval is called on the body of a user defined procedures
# create a new environment


# I can really see why scheme is so cool,
# since everything is represented as a pair
# It is really easy to program the language

# applying a user defined procedure
# we create a new frame where all the formal parameters
# are bound to argument names
# the parent of this new frame is the environment of the procedure
# then eval the body of the procedure in the env which starts with the new fram


#=========================================

# Frames and environments
# each frame is defined with a parent
# if a parent has no parent, then it is the global frame




