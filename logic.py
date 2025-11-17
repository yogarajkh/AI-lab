
Tanmay Talanki Rajeeva
4:26 PM (0 minutes ago)
to me

from itertools import product



def pl_true(sentence, model):
    """Evaluate propositional logic sentence under a model."""
    if isinstance(sentence, str):
        return model[sentence]
    op = sentence[0]
    if op == 'not':
        return not pl_true(sentence[1], model)
    elif op == 'and':
        return pl_true(sentence[1], model) and pl_true(sentence[2], model)
    elif op == 'or':
        return pl_true(sentence[1], model) or pl_true(sentence[2], model)
    elif op == 'implies':
        return (not pl_true(sentence[1], model)) or pl_true(sentence[2], model)
    elif op == 'iff':
        return pl_true(sentence[1], model) == pl_true(sentence[2], model)
    else:
        raise ValueError(f"Unknown operator: {op}")

def get_symbols(sentence):
    """Extract propositional symbols recursively."""
    if isinstance(sentence, str):
        return {sentence}
    elif isinstance(sentence, tuple):
        s = set()
        for part in sentence[1:]:
            s |= get_symbols(part)
        return s
    return set()

def tt_entails(KB, alpha):
    """Return True if KB entails alpha, and print a full truth table."""
    symbols = sorted(list(get_symbols(KB) | get_symbols(alpha)))

    print("\nPropositional Inference: Enumeration Method")
    print("KB = (A ∨ B) ∧ (¬A ∨ C)")
    print("α  = B\n")

    # Print header
    print(" A  |  B  |  C  | A∨B | ¬A∨C |  KB  |  α  ")
    print("-------------------------------------------")

    entails = True
    for values in product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))

        # Subformulas
        AorB = pl_true(('or', 'A', 'B'), model)
        notA_or_C = pl_true(('or', ('not', 'A'), 'C'), model)
        KB_val = pl_true(('and', ('or', 'A', 'B'), ('or', ('not', 'A'), 'C')), model)
        alpha_val = pl_true('B', model)

        print(f" {str(model['A']):<5}| {str(model['B']):<5}| {str(model['C']):<5}| {str(AorB):<5}| {str(notA_or_C):<6}| {str(KB_val):<5}| {str(alpha_val):<5}")

        if KB_val and not alpha_val:
            entails = False

    print("-------------------------------------------")
    print("Does KB entail α", entails)
    return entails


KB = ('and', ('or', 'A', 'B'), ('or', ('not', 'A'), 'C'))
alpha = 'B'

tt_entails(KB, alpha)
