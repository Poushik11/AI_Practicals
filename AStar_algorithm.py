# A Star
from collections import deque
initial_state = [
    [1, 2, 3, 4],
    [5, 6, 0, 7],
    [9, 10, 11, 8],
    [13, 14, 15, 12]
]

goal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]
# initial_state = [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 15, 14, 0]
#     ]
# goal = [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 0]
#     ]

def goal_state(state):
    # goal = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    #     [13, 14, 15, 0]
    # ]

    return state == goal

def find_zero(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j

def generate(state):
    successors = []
    empty_i, empty_j = find_zero(state)

    def move(direction):
        new_i, new_j = empty_i + direction[0], empty_j + direction[1]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
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

def calculate_heuristic(state):
    misplaced_tiles = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles


def a_star(initial_state):
    open_list = deque([(initial_state, 0, calculate_heuristic(initial_state))])
    explored = set()
    level = 0

    while open_list:
        level_size = len(open_list)
        print(f"Level {level} - Number of states: {level_size}:")

        for _ in range(level_size):
            current_state, current_level, current_heuristic = open_list.popleft()
            total_sum = current_level + current_heuristic

            print(f"Level {level}, State Heuristic: {current_heuristic}, Total Sum: {total_sum}:")
            for row in current_state:
                print(row)
            print()

            if goal_state(current_state):
                print("Goal state found.")
                for row in current_state:
                    print(row)
                print(f"Total levels: {level}")
                return

            explored.add(tuple(map(tuple, current_state)))

            successors = generate(current_state)
            for s in successors:
                if tuple(map(tuple, s)) not in explored and s not in [(state, _, _) for state, _, _ in open_list]:
                    heuristic_value = calculate_heuristic(s)
                    open_list.append((s, current_level + 1, heuristic_value))

        open_list = deque(sorted(open_list, key=lambda x: x[1] + x[2]))
        level += 1

a_star(initial_state)