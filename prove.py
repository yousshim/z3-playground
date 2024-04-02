from z3 import *


# prove that binary search always terminates
# this can be proven by the fact that r - l
# is always decreasing regardless of the
# executed branch in the loop

l, r = Ints("l r")

preconditions = And([
    l >= 0,
    r > l, # assume the range is not empty
])

mid = (l + r) / 2
termination = And([
    (r - l) > (mid - l),
    (r - l) > (r - (mid + 1)),
])

claim = Implies(preconditions, termination)

prove(claim)
