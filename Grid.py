import numpy as np
import matplotlib.pyplot as plt

class GridMaker:

    def ObstacleRect(x1, x2, y1, y2, map):
        for i in range(x1, x2):
            for j in range(y1, y2):
                map[i,j] = 1
        return map


    def Grid(self):
        print("Welcome to implementation of RRT Path Planning Algorithm! \n")
        print("Do you want to continue with default maze or create your own maze? Enter 0 or 1 \n")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            grid = np.zeros((1800, 1200))
            grid = self.DefaultGrid(grid)
            print("The size of current maze (x,y) is: ", grid.shape[1]," X ", grid.shape[0])
            start_x, start_y = [int(item) for item in input("Enter the starting point (x then y): ").split()]
            goal_x, goal_y = [int(item) for item in input("Enter the goal point (x then y): ").split()]

        elif choice == 1:
            mapSizex, mapSizey = [int(item) for item in input("Enter mapsize (x then y)").split()]
            n = int(input("Enter number of obstacles: "))
            grid = np.zeros((mapSizey, mapSizex))
            vertex = []
            for i in range(1, n+1):
                 vertexIn =  [int(item) for item in input(f"Enter the vertices (x1 x2 y1 y3) of Obstacle {i} in order (Assumption x1 == x4 & x2==x3, and y1 == y2 & y3==y4): ").split()]
                 vertex.append(vertexIn)
                 for vertexind in vertex:
                     grid = GridMaker.ObstacleRect(vertexind[0], vertexind[1], vertexind[2], vertexind[3], grid)
            print("The size of current maze (x,y) is: ", grid.shape[1]," X ", grid.shape[0])
            plt.imshow(grid, cmap='binary')
            plt.show()
            start_x, start_y = [int(item) for item in input("Enter the starting point (x then y): ").split()]
            goal_x, goal_y = [int(item) for item in input("Enter the goal point (x then y): ").split()]


        else:
            print("Invalid choice. Please try again.")
            self.Grid()

        return [grid, start_x, start_y, goal_x, goal_y]
    
    def DefaultGrid(self, map):
        vertex = [[500,1000,200,600], [200,800,900,1100], [1250, 1700,400, 600]]
        for vert in vertex:
            for i in range(vert[0], vert[1]):
                for j in range(vert[2], vert[3]):
                    map[i,j] = 1   
        return map
