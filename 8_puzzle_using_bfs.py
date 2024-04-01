# 8 Puzzle problem using bfs
from collections import deque

def goal_state(state):
    return state == [[1, 6, 3], [2, 4, 5], [ 7, 8, 0]]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_successors(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            successors.append(new_state)

    move_up = (-1, 0)
    move_down = (1, 0)
    move_left = (0, -1)
    move_right = (0, 1)

    move(move_up)
    move(move_down)
    move(move_left)
    move(move_right)

    return successors


def bfs(initial_state):
    open_list = deque([(initial_state, 0)])
    explored = set()

    while open_list:
        current_state, level = open_list.popleft()

        print(f"Level {level}:")
        for row in current_state:
            print(row)
        print()

        if goal_state(current_state):
            print("gaol state found.")
            for row in current_state:
                print(row)
            print(f"total levels: {level}")
            return

        explored.add(tuple(map(tuple, current_state)))

        successors = generate_successors(current_state)
        for s in successors:
            if tuple(map(tuple, s)) not in explored and s not in [state for state, _ in open_list]:
                open_list.append((s, level + 1))

    print("No solution found.")

#project idx
# initial_state = [[1, 6, 0], [2, 4, 3], [ 7, 8,5]]
# initial_state = [[1, 0, 6], [2, 4, 3], [ 7, 8,5]]
# initial_state = [[1, 6, 0], [2, 3, 7], [ 4, 8,5]]
# initial_state = [[7, 6, 0], [2, 4, 3], [ 1, 8,5]]
initial_state = [[1, 6, 0], [2, 4, 3], [ 7, 8,5]]
bfs(initial_state)
