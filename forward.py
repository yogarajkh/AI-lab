def is_variable(x):
    return x.islower()

def parse_predicate(s):
    name, args = s.split("(")
    args = args[:-1].split(",")
    return name, args

def substitute(pred, subst):
    name, args = parse_predicate(pred)
    new_args = []
    for a in args:
        new_args.append(subst.get(a, a))
    return name + "(" + ",".join(new_args) + ")"

def unify(p1, p2):
    name1, args1 = parse_predicate(p1)
    name2, args2 = parse_predicate(p2)
    if name1 != name2 or len(args1) != len(args2):
        return None
    subst = {}
    for a, b in zip(args1, args2):
        if a == b:
            continue
        if is_variable(a):
            subst[a] = b
        elif is_variable(b):
            subst[b] = a
        else:
            return None
    return subst

def forward_chaining(facts, rules):
    new_facts = set(facts)
    changed = True

    while changed:
        changed = False

        for conds, head in rules:
            for fact in list(new_facts):
                subst = unify(conds[0], fact)
                if subst is None:
                    continue

                valid = True
                for c in conds[1:]:
                    needed = substitute(c, subst)
                    if needed not in new_facts:
                        valid = False
                        break

                if valid:
                    inferred = substitute(head, subst)
                    if inferred not in new_facts:
                        new_facts.add(inferred)
                        changed = True

    return new_facts




facts = {
    "parent(john,mary)",
    "parent(mary,alice)"
}

rules = [
    (["parent(x,y)"], "ancestor(x,y)"),
    (["parent(x,y)", "ancestor(y,z)"], "ancestor(x,z)")
]

result = forward_chaining(facts, rules)
print("Inferred Facts:")
for f in sorted(result):
    print(f)
