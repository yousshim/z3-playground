from z3 import *


def FreshBitVec(name: str, size: int) -> BitVecRef:
    return FreshConst(BitVecSort(size), name)


def sorted(arr: FuncDeclRef) -> BoolRef | QuantifierRef:
    i = FreshBitVec("i", 32)
    j = FreshBitVec("j", 32)
    return ForAll([i, j], Implies(i > j, arr(i) >= arr(j)))


def in_range(
    arr: FuncDeclRef, target: ArithRef, l: BitVecRef, r: BitVecRef
) -> BoolRef | QuantifierRef:
    i = FreshBitVec("i", 32)
    return Exists(i, And(arr(i) == target, i >= l, i < r))


# prove that binary search always terminates
# this can be proven by the fact that r - l
# is always decreasing regardless of the
# executed branch in the loop

l, r = BitVecs("l r", 32)
target = Int("target")
arr = Function("arr", BitVecSort(32), IntSort())

preconditions = And(
    [
        l >= 0,
        r > l,  # assume the start range is not empty
        sorted(arr),  # assum the arris is sorted
        in_range(arr, target, l, r),  # assume target exists in start range
    ]
)

mid = l + (r - l) / 2
termination = And(
    [
        (r - l) > (mid - l),
        (r - l) > (r - (mid + 1)),
    ]
)

# prove that the target can always be found between l and r
# regardless of which code branch gets executed
loop_invariant = And(
    [
        Implies(target < arr(mid), in_range(arr, target, l, mid)),
        Implies(target > arr(mid), in_range(arr, target, mid + 1, r)),
    ]
)

claim = Implies(preconditions, termination)

prove(claim)

claim = Implies(preconditions, loop_invariant)

prove(claim)
