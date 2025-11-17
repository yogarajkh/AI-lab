import random
from collections import deque

def initialize_puzzle():
    numbers = list(range(9))
    random.shuffle(numbers)
    puzzle = [numbers[i:i+3] for i in range(0, 9, 3)]

    
    inversions = 0
    flat_puzzle = [item for sublist in puzzle for item in sublist if item != 0]
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1

    blank_row = -1
    for r in range(3):
        for c in range(3):
            if puzzle[r][c] == 0:
                blank_row = r
                break
        if blank_row != -1:
            break

    is_solvable = False
    if blank_row in [0, 2]:
        if inversions % 2 == 0:
            is_solvable = True
    elif blank_row == 1:
        if inversions % 2 != 0:
            is_solvable = True

    if not is_solvable:
        
        indices = []
        for r in range(3):
            for c in range(3):
                if puzzle[r][c] != 0:
                    indices.append((r, c))
                    if len(indices) == 2:
                        break
            if len(indices) == 2:
                break
        r1, c1 = indices[0]
        r2, c2 = indices[1]
        puzzle[r1][c1], puzzle[r2][c2] = puzzle[r2][c2], puzzle[r1][c1]

    return puzzle

def display_puzzle(puzzle):
    for row in puzzle:
        print("|---|---|---|")
        print("|", end=" ")
        for cell in row:
            if cell == 0:
                print("   |", end=" ")
            else:
                print(f" {cell} |", end=" ")
        print()
    print("|---|---|---|")

def find_blank(puzzle):
    for r in range(3):
        for c in range(3):
            if puzzle[r][c] == 0:
                return r, c
    return -1, -1

def get_possible_moves(puzzle):
    blank_r, blank_c = find_blank(puzzle)
    possible_moves = []
    if blank_r > 0:
        possible_moves.append("Up")
    if blank_r < 2:
        possible_moves.append("Down")
    if blank_c > 0:
        possible_moves.append("Left")
    if blank_c < 2:
        possible_moves.append("Right")
    return possible_moves

def perform_move(puzzle, move):
    new_puzzle = [list(row) for row in puzzle]
    blank_r, blank_c = find_blank(new_puzzle)

    if move == "Up":
        move_r, move_c = blank_r - 1, blank_c
    elif move == "Down":
        move_r, move_c = blank_r + 1, blank_c
    elif move == "Left":
        move_r, move_c = blank_r, blank_c - 1
    elif move == "Right":
        move_r, move_c = blank_r, blank_c + 1

    new_puzzle[blank_r][blank_c], new_puzzle[move_r][move_c] = new_puzzle[move_r][move_c], new_puzzle[blank_r][blank_c]
    return new_puzzle

def check_win(puzzle):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return puzzle == goal_state

def solve_puzzle_bfs(initial_puzzle):
    queue = deque([(initial_puzzle, [])])  # BFS queue
    visited = set()

    def tuple_representation(puzzle):
        return tuple(tuple(row) for row in puzzle)

    visited.add(tuple_representation(initial_puzzle))

    while queue:
        current_puzzle, path = queue.popleft()

        if check_win(current_puzzle):
            return path

        possible_moves = get_possible_moves(current_puzzle)
        for move in possible_moves:
            next_puzzle = perform_move(current_puzzle, move)
            next_state = tuple_representation(next_puzzle)

            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_puzzle, path + [move]))

    return None


initial_puzzle = initialize_puzzle()

print("Initial Puzzle:")
display_puzzle(initial_puzzle)

print("\nSolving the puzzle using BFS...")

solution_path = solve_puzzle_bfs(initial_puzzle)

if solution_path:
    print(f"\nSolution found in {len(solution_path)} moves:\n")
    current_puzzle = [list(row) for row in initial_puzzle]
    for i, move in enumerate(solution_path):
        current_puzzle = perform_move(current_puzzle, move)
        print(f"\nStep {i + 1}: Move {move}")
        display_puzzle(current_puzzle)
    print("\nCongratulations the puzzle is solvedf")
else:
    print("\nNo solution found.")


iddfs


import random

def initialize_puzzle():
    numbers = list(range(9))
    random.shuffle(numbers)
    puzzle = [numbers[i:i+3] for i in range(0, 9, 3)]
    inversions = 0
    flat_puzzle = [item for sublist in puzzle for item in sublist if item != 0]
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    blank_row = -1
    for r in range(3):
        for c in range(3):
            if puzzle[r][c] == 0:
                blank_row = r
                break
        if blank_row != -1:
            break
    is_solvable = False
    if blank_row in [0, 2]:
        if inversions % 2 == 0:
            is_solvable = True
    elif blank_row == 1:
        if inversions % 2 != 0:
            is_solvable = True
    if not is_solvable:
        for r1 in range(3):
            for c1 in range(3):
                if puzzle[r1][c1] != 0:
                    for r2 in range(3):
                        for c2 in range(3):
                            if puzzle[r2][c2] != 0 and (r1, c1) != (r2, c2):
                                puzzle[r1][c1], puzzle[r2][c2] = puzzle[r2][c2], puzzle[r1][c1]
                                return puzzle
    return puzzle

def display_puzzle(puzzle):
    for row in puzzle:
        print("|---|---|---|")
        print("|", end=" ")
        for cell in row:
            if cell == 0:
                print("   |", end=" ")
            else:
                print(f" {cell} |", end=" ")
        print()
    print("|---|---|---|")

def find_blank(puzzle):
    for r in range(3):
        for c in range(3):
            if puzzle[r][c] == 0:
                return r, c
    return -1, -1

def get_possible_moves(puzzle):
    blank_r, blank_c = find_blank(puzzle)
    possible_moves = []
    if blank_r > 0: possible_moves.append("Up")
    if blank_r < 2: possible_moves.append("Down")
    if blank_c > 0: possible_moves.append("Left")
    if blank_c < 2: possible_moves.append("Right")
    return possible_moves

def perform_move(puzzle, move):
    new_puzzle = [list(row) for row in puzzle]
    blank_r, blank_c = find_blank(new_puzzle)
    if move == "Up": move_r, move_c = blank_r - 1, blank_c
    elif move == "Down": move_r, move_c = blank_r + 1, blank_c
    elif move == "Left": move_r, move_c = blank_r, blank_c - 1
    elif move == "Right": move_r, move_c = blank_r, blank_c + 1
    new_puzzle[blank_r][blank_c], new_puzzle[move_r][move_c] = new_puzzle[move_r][move_c], new_puzzle[blank_r][blank_c]
    return new_puzzle

def check_win(puzzle):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return puzzle == goal_state

def tuple_representation(puzzle):
    return tuple(tuple(row) for row in puzzle)

def depth_limited_search(puzzle, path, depth, visited):
    if check_win(puzzle):
        return path
    if depth == 0:
        return None
    visited.add(tuple_representation(puzzle))
    for move in get_possible_moves(puzzle):
        new_puzzle = perform_move(puzzle, move)
        state = tuple_representation(new_puzzle)
        if state not in visited:
            result = depth_limited_search(new_puzzle, path + [move], depth - 1, visited)
            if result is not None:
                return result
    return None

def solve_puzzle_iddfs(initial_puzzle, max_depth=30):
    for depth in range(max_depth + 1):
        visited = set()
        result = depth_limited_search(initial_puzzle, [], depth, visited)
        if result is not None:
            return result
    return None

if __name__ == "__main__":
    initial_puzzle = initialize_puzzle()
    print("Initial Puzzle:")
    display_puzzle(initial_puzzle)
    print("\nSolving the puzzle using IDDFS...")
    solution_path = solve_puzzle_iddfs(initial_puzzle, max_depth=30)
    if solution_path:
        print(f"\nSolution found in {len(solution_path)} moves:\n")
        current_puzzle = [list(row) for row in initial_puzzle]
        for i, move in enumerate(solution_path):
            current_puzzle = perform_move(current_puzzle, move)
            print(f"\nStep {i + 1}: Move {move}")
            display_puzzle(current_puzzle)
        print("\n Congratulations, the puzzle is solved!")
    else:
        print("\nNo solution found within depth limit.")

