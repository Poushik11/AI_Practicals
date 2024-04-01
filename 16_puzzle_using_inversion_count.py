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

def getInvCount(arr):
    inv_count = 0
    empty = -1
    for i in range(0, 16):
        for j in range(i + 1, 16):
            if arr[j] != empty and arr[i] != empty and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle) :
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    return (inv_count % 2 == 0)


def goal_state(state):

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


def bfs(initial_state):
    open_list = deque([(initial_state, 0)])
    explored = set()
    level = 0

    while open_list:
        level_size = len(open_list)
        print(f"Level {level} - Number of states: {level_size}:")

        for _ in range(level_size):
            current_state, _ = open_list.popleft()
            print(f"Level {level}:")
            for row in current_state:
               print(row)
            print()

            if goal_state(current_state):
                print("Goal state found.")
                for row in current_state:
                    print(row)
                print(f"total levels: {level}")
                return

            explored.add(tuple(map(tuple, current_state)))

            successors = generate(current_state)
            for s in successors:
                if tuple(map(tuple, s)) not in explored and s not in [state for state, _ in open_list]:
                    open_list.append((s, level + 1))

        level += 1

inv_goal_state=isSolvable(goal)

if(inv_goal_state%2==0):
   if(isSolvable(initial_state)):
      bfs(initial_state)
   else:
      print("Not solvable")

if(inv_goal_state%2==1):
   if(isSolvable(initial_state)):
      print("Not solvable")
   else:
      bfs(initial_state)

# Solvable
