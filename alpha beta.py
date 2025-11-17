import math

tree = [
    [21, 5],
    [15, 11],
    [8, 9],
    [13, 5],
    [13, 12],
    [13, 14],
    [7, 10],
    [13, 10]
]

leaf_labels = [
    ["A", "B"], ["C", "D"], ["E", "F"], ["G", "H"],
    ["I", "J"], ["K", "L"], ["M", "N"], ["O", "P"]
]

pruned_nodes = []

def min_value(leaves, alpha, beta, labels):
    v = math.inf
    for i, val in enumerate(leaves):
        v = min(v, val)
        if v <= alpha:
            pruned_nodes.extend(labels[i + 1:])
            break
        beta = min(beta, v)
    return v

def alpha_beta_search():
    alpha = -math.inf
    beta = math.inf
    max_value = -math.inf
    min_values = []

    for i, leaves in enumerate(tree):
        v = min_value(leaves, alpha, beta, leaf_labels[i])
        min_values.append(v)
        if v > max_value:
            max_value = v
        alpha = max(alpha, max_value)

    print("Values at each MIN node:", min_values)
    print("Root (MAX) value:", max_value)
    print("Pruned nodes:", pruned_nodes)

if __name__ == "__main__":
    alpha_beta_search()
