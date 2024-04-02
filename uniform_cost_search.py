from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the possible moves
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

# Define a function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = (state[i][j] - 1) // 3, (state[i][j] - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Define a function to check if a state is the goal state
def is_goal_state(state):
    return state == goal_state

# Define a function to generate successor states
def generate_successors(state):
    successors = []
    zero_row, zero_col = find_zero(state)
    for move in moves[zero_row * 3 + zero_col]:
        new_state = [row[:] for row in state]
        new_row, new_col = move // 3, move % 3
        new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
        successors.append(new_state)
    return successors

# Define the UCS algorithm
def uniform_cost_search(initial_state):
    frontier = PriorityQueue()
    explored = set()
    frontier.put((0, initial_state))
    
    while not frontier.empty():
        cost, current_state = frontier.get()
        
        if is_goal_state(current_state):
            return current_state
        
        explored.add(tuple(map(tuple, current_state)))
        
        for successor in generate_successors(current_state):
            if tuple(map(tuple, successor)) not in explored:
                priority = cost + 1
                frontier.put((priority, successor))
                explored.add(tuple(map(tuple, successor)))
    
    return None

# Define a function to find the position of the zero element
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Example usage:
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
goal = uniform_cost_search(initial_state)
if goal:
    print("Goal state found:")
    for row in goal:
        print(row)
else:
    print("Goal state not found.")
