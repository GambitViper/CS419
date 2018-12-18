import random, csv

LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
actions = [DOWN, RIGHT, UP, LEFT]

# Setup for pipe_world reading

lines = [line.rstrip() for line in open('pipe_world.txt')]

state_actions = [[[0 for i in range(4)] 
                     for j in range(len(lines[0]))] 
                     for k in range(len(lines))]

# Translating pipe_world into a reward array

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

# Loop check conditions for episode ending during training

def reachedGoal(state):
    return state == goal

def hitMine(state):
    return reward[state[0]][state[1]] == -100

def exceededSteps(steps):
    return steps == len(reward[0]) * len(reward)

# Regular Q-Learning functions

def maxQ_index(state):
    x, y = state[0], state[1]
    maxq = 0
    for a in range(1, 4):
        if state_actions[x][y][a] > state_actions[x][y][maxq]:
            maxq = a
    return maxq

def maxQ(state):
    x, y = state[0], state[1]
    return state_actions[x][y][maxQ_index(state)]

def chooseAction(state, epsilon):
    rand = random.random()
    if rand < epsilon:
        return random.choice(actions)
    else:
        return maxQ_index(state)

# Q-Learning with feature functions

def bestAction_features(state, weights):
    bestVal = weights_cross_features(state, weights, 0)
    bestAction = 0
    for action in range(1,4):
        checkVal = weights_cross_features(state, weights, action)
        if checkVal > bestVal:
            bestVal = checkVal
            bestAction = action
    return bestAction

def chooseAction_feature(state, epsilon, weights):
    rand = random.random()
    if rand < epsilon:
        return random.choice(actions)
    else:
        return bestAction_features(state, weights)
        
def weights_cross_features(state, weights, action):
    w1, w2 = weights[0], weights[1]
    f1 = feature1(takeActionNoSlip(state, action))
    f2 = feature2(state, action)
    return ( w1 * f1 ) + ( w2 * f2 )

def maxQ_features(state, weights):
    action = bestAction_features(state, weights)
    return weights_cross_features(state, weights, action)

# State transformation function for taking actions

def isAllowed(state):
    x, y = state[0], state[1]
    return 0 <= x < len(reward) and 0 <= y < len(reward[0])

def up(state):
    newstate = list(state)
    newstate[0] = state[0] - 1
    newstate[1] = state[1]
    return newstate

def down(state):
    newstate = list(state)
    newstate[0] = state[0] + 1
    newstate[1] = state[1]
    return newstate

def right(state):
    newstate = list(state)
    newstate[0] = state[0]
    newstate[1] = state[1] + 1
    return newstate

def left(state):
    newstate = list(state)
    newstate[0] = state[0]
    newstate[1] = state[1] - 1
    return newstate

# Action taking function with no slippage to consider features

def takeActionNoSlip(state, action):
    newstate = list(state)
    if action == UP:
        newstate = up(state)
    elif action == DOWN:
        newstate = down(state)
    elif action == LEFT:
        newstate = left(state)
    elif action == RIGHT:
        newstate = right(state)
    if isAllowed(newstate):
        return tuple(newstate)
    else:
        return state

# Action taking function with slippage used for evaluating both policies

def takeAction(state, action):
    newstate = list(state)
    rand = random.random()
    slip = rand <= 0.2
    if action == UP:
        newstate = up(state)
        if slip:
            if random.random() < 0.5:
                newstate[1] = state[1] - 1
            else:
                newstate[1] = state[1] + 1
    elif action == DOWN:
        newstate = down(state)
        if slip:
            if random.random() < 0.5:
                newstate[1] = state[1] - 1
            else:
                newstate[1] = state[1] + 1
    elif action == LEFT:
        newstate = left(state)
        if slip:
            if random.random() < 0.5:
                newstate[0] = state[0] - 1
            else:
                newstate[0] = state[0] + 1
    elif action == RIGHT:
        newstate = right(state)
        if slip:
            if random.random() < 0.5:
                newstate[0] = state[0] - 1
            else:
                newstate[0] = state[0] + 1
    if isAllowed(newstate):
        return tuple(newstate)
    else:
        return state

# Implementation of regular q-learning

q_learning = []

def test_qlearning():
    total_reward = 0
    for _ in range(50):
        s = tuple([start_x, start_y])
        steps = 0
        while not reachedGoal(s) and not hitMine(s) and not exceededSteps(steps):
            action = maxQ_index(s)
            sn = takeAction(s, action)
            total_reward += reward[sn[0]][sn[1]]
            s = sn
            steps += 1
    return total_reward / 50

goal = tuple([goal_x, goal_y])
episodes = 10000
epsilon = 0.9
alpha = 0.9

for episode in range(episodes):
    s = tuple([start_x, start_y])
    steps = 0
    if episode != 0 and episode % 100 == 0:
        q_learning.append(test_qlearning())
    while not reachedGoal(s) and not hitMine(s) and not exceededSteps(steps):
        action = chooseAction(s, epsilon)
        sn = takeAction(s, action)
        state_actions[s[0]][s[1]][action] += alpha * (reward[sn[0]][sn[1]] + (0.9) *  maxQ(sn) - state_actions[s[0]][s[1]][action])
        s = sn
        steps += 1
    alpha = 0.9/(episode/1000 + 1)
    epsilon = 0.9/(episode/200 + 1)

# Implementation of Feature based q-learning

qf_learning = []

def test_qlearning_features():
    total_reward = 0
    for _ in range(50):
        s = tuple([start_x, start_y])
        steps = 0
        while not reachedGoal(s) and not hitMine(s) and not exceededSteps(steps):
            action = bestAction_features(s, weights)
            sn = takeAction(s, action)
            total_reward += reward[sn[0]][sn[1]]
            s = sn
            steps += 1
    return total_reward / 50

# Feature finding functions

def feature1(state):
    x, y = state[0], state[1]
    return ( abs(x - goal_x) + abs(y - goal_y) ) / ( goal_x + goal_y )

def feature2(state, action):
    y = state[1]
    inverseDistLeft = 1 / (y + 1)
    inverseDistRight = 1 / (len(reward[0]) - y)
    if action == LEFT:
        return inverseDistLeft
    elif action == RIGHT:
        return inverseDistRight
    elif action == UP or action == DOWN:
        return min(inverseDistLeft, inverseDistRight)

goal = tuple([goal_x, goal_y])
episodes = 10000
epsilon = 0.9
alpha = 0.9

w1 , w2 = 0.0, 0.0
weights = tuple([w1, w2])

for episode in range(episodes):
    s = tuple([start_x, start_y])
    steps = 0
    if episode != 0 and episode % 100 == 0:
        qf_learning.append(test_qlearning_features())
    while not reachedGoal(s) and not hitMine(s) and not exceededSteps(steps):
        action = chooseAction_feature(s, epsilon, weights)
        sn = takeAction(s, action)
        newWeights = list(weights)
        delta = reward[sn[0]][sn[1]] + (0.9) * maxQ_features(sn, weights) - weights_cross_features(s, weights, action)
        newWeights[0] += alpha * delta * feature1(sn)
        newWeights[1] += alpha * delta * feature2(s, action)
        weights = tuple(newWeights)
        s = sn
        steps += 1
    alpha = 0.9/(episode/1000 + 1)
    epsilon = 0.9/(episode/200 + 1)

# Dual purpose policy printer

def print_policy(state_actions, weights, isFeature):
    for x in range(len(state_actions)):
        for y in range(len(state_actions[0])):
            state = tuple([x,y])
            if reward[x][y] == -100:
                print("M",end='')
            elif state == goal:
                print("G",end='')
            else:
                if isFeature:
                    action = bestAction_features(state, weights)
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

# ~~~ CSV file writer ~~~
writer = csv.writer(open("results.csv", 'w'))
writer.writerow(q_learning)
writer.writerow(qf_learning)

print("Q-Learning policy")
print_policy(state_actions, weights, False)
# print(q_learning)
print("Q-Learning with Features policy")
print_policy(state_actions, weights, True)
# print(qf_learning)