import random

DOWN, LEFT, RIGHT, UP = 0, 1, 2, 3
actions = [DOWN, LEFT, RIGHT, UP]

lines = [line.rstrip() for line in open('pipe_world.txt')]

state_actions = [[[0 for i in range(4)] 
                     for j in range(len(lines[0]))] 
                     for k in range(len(lines))]

start_x, start_y, goal_x, goal_y = 0, 0, 0, 0
reward = [[-1 for x in range(len(lines[0]))] for y in range(len(lines))]

for x in range(len(lines)):
    for y in range(len(lines[0])):
        check_line = list(lines[x])
        if check_line[y] == 'S':
            start_x = x
            start_y = y
        if check_line[y] == 'G':
            goal_x = x
            goal_y = y
            reward[x][y] = 0
        if check_line[y] == 'M':
            reward[x][y] = -100

goal = tuple([goal_x, goal_y])
episodes = 10000
epsilon = 0.9
alpha = 0.9

def reachedGoal(state):
    return state == goal

def hitMine(state):
    return reward[state[0]][state[1]] == -100

def exceededSteps(steps):
    return steps == len(reward[0]) * len(reward)

def maxQ_index(state):
    x, y = state[0], state[1]
    maxq = 0
    for a in range(1, 4):
        if state_actions[x][y][a] > state_actions[x][y][maxq]:
            maxq = a
    return maxq

def chooseAction(state, epsilon):
    rand = random.random()
    if rand < epsilon:
        return random.choice(actions)
    else:
        return maxQ_index(state)        

def isAllowed(state):
    x, y = state[0], state[1]
    return 0 <= x < len(reward) and 0 <= y < len(reward[0])

def takeAction(state, action):
    newstate = list(state)
    rand = random.random()
    slip = rand <= 0.2
    if action == UP:
        newstate[0] = state[0] - 1
        newstate[1] = state[1]
        if slip:
            if random.random() < 0.5:
                newstate[1] = state[1] - 1
            else:
                newstate[1] = state[1] + 1
    elif action == DOWN:
        newstate[0] = state[0] + 1
        newstate[1] = state[1]
        if slip:
            if random.random() < 0.5:
                newstate[1] = state[1] - 1
            else:
                newstate[1] = state[1] + 1
    elif action == LEFT:
        newstate[0] = state[0]
        newstate[1] = state[1] - 1
        if slip:
            if random.random() < 0.5:
                newstate[0] = state[0] - 1
            else:
                newstate[0] = state[0] + 1
    elif action == RIGHT:
        newstate[0] = state[0]
        newstate[1] = state[1] + 1
        if slip:
            if random.random() < 0.5:
                newstate[0] = state[0] - 1
            else:
                newstate[0] = state[0] + 1
    if isAllowed(newstate):
        return tuple(newstate)
    else:
        return state

def maxQ(state):
    x, y = state[0], state[1]
    return state_actions[x][y][maxQ_index(state)]

for episode in range(episodes):
    s = tuple([start_x, start_y])
    steps = 0
    while not reachedGoal(s) and not hitMine(s) and not exceededSteps(steps):
        action = chooseAction(s, epsilon)
        sn = takeAction(s, action)
        state_actions[s[0]][s[1]][action] += alpha * (reward[sn[0]][sn[1]] + (0.9) *  maxQ(sn) - state_actions[s[0]][s[1]][action])
        s = sn
        steps += 1
    alpha = 0.9/(episode/1000 + 1)
    epsilon = 0.9/(episode/200 + 1)

def print_policy(state_actions):
    for x in range(len(state_actions)):
        for y in range(len(state_actions[0])):
            state = tuple([x,y])
            if reward[x][y] == -100:
                print("M",end='')
            elif state == goal:
                print("G",end='')
            else:
                action = maxQ_index(state)
                if action == UP:
                    print("U",end='')
                elif action == DOWN:
                    print("D",end='')
                elif action == LEFT:
                    print("L",end='')
                elif action == RIGHT:
                    print("R",end='')
        print("")

print_policy(state_actions)
print(state_actions)