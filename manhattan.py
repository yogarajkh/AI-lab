from typing import List, Optional, Tuple

State = List[Optional[int]]

def goal_state() -> State:
    return [1,2,3,4,5,6,7,8,None]

def manhattan_distance(state: State) -> int:
    g = goal_state()
    total = 0
    for i, tile in enumerate(state):
        if tile is None:
            continue
        gi = g.index(tile)
        r1, c1 = divmod(i, 3)
        r2, c2 = divmod(gi, 3)
        total += abs(r1 - r2) + abs(c1 - c2)
    return total

def print_board(state: State):
    print("+----+----+----+")
    for i in range(0, 9, 3):
        row = state[i:i+3]
        cells = ["  " if x is None else f"{x:>2}" for x in row]
        print("| {} | {} | {} |".format(*cells))
        print("+----+----+----+")
    print()

def neighbors(state: State) -> List[Tuple[State, str]]:
    blank = state.index(None)
    r, c = divmod(blank, 3)
    moves = [(-1,0,"Up"), (1,0,"Down"), (0,-1,"Left"), (0,1,"Right")]
    results = []
    for dr, dc, direction in moves:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr*3 + nc
            new_state = state[:]
            new_state[blank], new_state[new_pos] = new_state[new_pos], new_state[blank]
            results.append((new_state, direction))
    return results

def hill_climbing_manhattan(start: State):
    current = start
    h = manhattan_distance(current)
    step = 0
    print(f"Step {step} (Total Manhattan Distance = {h}):")
    print_board(current)

    while True:
        if current == goal_state():
            print("Reached goal with Manhattan Distance = 0\n")
            return current

        successors = neighbors(current)
        print(f"Successors of step {step}:")
        for nb, direction in successors:
            hn = manhattan_distance(nb)
            print(f"Move: Blank {direction}")
            print_board(nb)
            print("Total Manhattan Distance =", hn)
        print()

        best_neighbor = None
        best_h = h
        best_move = None
        for nb, direction in successors:
            hn = manhattan_distance(nb)
            if hn < best_h:
                best_h = hn
                best_neighbor = nb
                best_move = direction

        if best_neighbor is None:
            print("No better successor found. Stuck at local minimum with Manhattan Distance =", h)
            return current

        step += 1
        current = best_neighbor
        h = best_h
        print(f"Chosen successor for step {step}: Blank moved {best_move} (Total Manhattan Distance = {h})")
        print_board(current)


if __name__ == "__main__":
    start = [1,2,3,4,5,6,None,7,8]
    hill_climbing_manhattan(start)
