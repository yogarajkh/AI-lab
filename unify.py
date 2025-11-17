def is_variable(x):
    return isinstance(x, str) and x.islower()

def unify(x, y, subst):
    if subst is None:
        return None
    if x in subst:
        return unify(subst[x], y, subst)
    if y in subst:
        return unify(x, subst[y], subst)
    if x == y:
        return subst
    if is_variable(x):
        subst[x] = y
        return subst
    if is_variable(y):
        subst[y] = x
        return subst
    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x) != len(y):
            return None
        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)
            if subst is None:
                return None
        return subst
    return None

term1 = ("f", "x", ("g", "y"))
term2 = ("f", ("g", "z"), ("g", "a"))

result = unify(term1, term2, {})
print("Result:", result)
