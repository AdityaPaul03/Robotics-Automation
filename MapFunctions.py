import math
import random
import numpy as np
import matplotlib.pyplot as plt


class MapFunctions:

    def __init__(self, grid, start, goal, numIterations, stepSize):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.numIterations = numIterations
        self.stepSize = stepSize

    def randomPoint(self):
        x = random.randint(1, self.grid.shape[1])
        y = random.randint(1, self.grid.shape[0])
        random_point = np.array([x, y])
        return random_point
        

    def nearestNode(self,random_point, Node_list):
        dist = math.inf
        for Node in Node_list:
            node_dist = ((random_point[0] - Node.x)**2 + (random_point[1] - Node.y)**2)**0.5
            if node_dist < dist:
                dist = node_dist
                nearest_node = Node
        return nearest_node


    def steeredPoint(self,nearest_node, random_point, step_size):
        slope = (nearest_node.y - random_point[1])/(nearest_node.x - random_point[0])
        theta = math.atan(slope)
        x = min(int(nearest_node.x + math.cos(theta)*step_size), self.grid.shape[1] - 1)
        y = min(int(nearest_node.y + math.sin(theta)*step_size), self.grid.shape[0] - 1)
        x = max(1, x)
        y = max(1, y)
        steered_point = np.array([x, y])
        return steered_point

    def checkObstacle(self,nearest_node, steered_point, step_size):
        intersection = False
        slope = (nearest_node.y - steered_point[1])/(nearest_node.x - steered_point[0])
        theta = math.atan(slope)
        for i in range(1, step_size):
            x = min(int(nearest_node.x + math.cos(theta)*i), self.grid.shape[1] - 1)
            y = min(int(nearest_node.y + math.sin(theta)*i), self.grid.shape[0] - 1)
            x = max(1, x)
            y = max(1, y)
            if self.grid[y][x] == 1:
                intersection = True
                break
            else:
                continue
        return intersection
    
