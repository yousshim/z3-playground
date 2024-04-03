from z3 import *


# prove that binary search always terminates
# this can be proven by the fact that r - l
# is always decreasing regardless of the
# executed branch in the loop

l, r = BitVecs("l r", 32)

preconditions = And([
    l >= 0,
    r > l, # assume the range is not empty
])

mid = l + (r - l) / 2
termination = And([
    (r - l) > (mid - l),
    (r - l) > (r - (mid + 1)),
])

claim = Implies(preconditions, termination)

prove(claim)
