# Required libraries
import numpy as np
import matplotlib.pyplot as plt

# Required files
from MapFunctions import MapFunctions
from Grid import GridMaker

# Make grid for RRT algorithm
grid = GridMaker()

[grid, start_x, start_y, goal_x, goal_y] = grid.Grid()

start = np.array([start_x, start_y]) #(x,y)
goal = np.array([goal_x, goal_y]) #(x,y)
numIterations = 200
stepSize = 100
goalRegion = plt.Circle((goal[0], goal[1]), stepSize, color='b', fill = False)
startRegion = plt.Circle((start[0], start[1]), stepSize, color='g', fill = False)

mf = MapFunctions(grid=grid, start=start, goal=goal, numIterations=numIterations, stepSize=stepSize)

fig = plt.figure("RRT Algorithm")
plt.imshow(grid, cmap='binary')
plt.plot(start[0],start[1],'ro')
plt.plot(goal[0],goal[1],'bo')
ax = fig.gca()
ax.add_patch(goalRegion)
ax.add_patch(startRegion)
plt.xlabel('X-axis $(m)$')
plt.ylabel('Y-axis $(m)$')

# Create nodes

class Node:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.parent = None
        self.children = []


Node_list = [] # contains (x,y) of each node
start_node = Node(start[0], start[1])
goal_node = Node(goal[0], goal[1])
Node_list.append(start_node) # elements are of Node class
step_size = 100
i = 0

# RRT Logic

while Node_list[-1].x != goal_node.x and Node_list[-1].y != goal_node.y:
    i += 1

    random_point = mf.randomPoint()
    nearest_node = mf.nearestNode(random_point, Node_list)
    steered_point = mf.steeredPoint(nearest_node, random_point, step_size)
    d = ((steered_point[0] - goal[0])**2 + (steered_point[1] - goal[1])**2)**0.5
    if d <= step_size:
        steered_point = goal
    intersection = mf.checkObstacle(nearest_node, steered_point, step_size)
    if intersection == True:
        continue
    else: 
        steered_node = Node(steered_point[0], steered_point[1])

    steered_node.parent = nearest_node
    nearest_node.children.append(steered_node)
    Node_list.append(steered_node)
    plt.plot(steered_point[0],steered_point[1],'ro')


def retracePath(Node_list, start_node):
    solution = []
    goal_node = Node_list[-1]
    solution.append(goal_node)
    parent = goal_node.parent
    while solution[-1] != start_node:
        for Node in Node_list:
            if Node == parent:
                solution.append(Node)
                parent = Node.parent
                break
            else: 
                continue
    return solution

def plotWaypoints(solution):
    previous_node = solution[0]
    for i in range(1, len(solution)):
        next_node = solution[i]
        plt.plot([previous_node.x, next_node.x], [previous_node.y, next_node.y],'go', linestyle="--")
        previous_node = next_node

solution = retracePath(Node_list, start_node)
plotWaypoints(solution)
plt.show()
