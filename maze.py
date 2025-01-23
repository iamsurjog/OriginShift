import random
import sys

class Point:
    """
    To create a point object which stores the directions it is positioned in. The __repr__ method is defined for debugging purposes
    """
    def __init__(self, pos, start = False, end = False, directions=None):
        self.start = start
        self.end = end
        if directions is None:
            #[[left, right], [up, down]] as negative y on pygame corresponds to
            self.directions = [[False, False], [False, False]]
        else:
            self.directions = directions

    def __repr__(self):
        return str(self.directions)

class Maze:
    def __init__(self, maze = None, size=(5, 5)):
        if maze is None:
            self.size = size
            self.maze = self.new_maze()
        else:
            self.maze = maze
            self.size = (len(maze[0]), len(maze[1]))
        self.origin = [0, 0]
        # for i in self.maze:
        #     print(i)
        # print(self.origin)
        # print(self.maze[self.origin[1]][self.origin[0]])
        # print("-" * 20)


    def new_maze(self):
        maze = [[Point(pos = (i, j)) for i in range(self.size[0])] for j in range(self.size[1])]

        # making all the lines pointing left
        for i in maze:
            for j in i:
                j.directions = [[True, False], [False, False]]

        # making the nodes on the left edge point up and not be able to go more to left
        for i in maze:
            i[0].directions = [[None, False], [True, False]]

        # puts the top edge of the maze
        for i in maze[0]:
            i.directions[1][0] = None

        # bottom edge
        for i in maze[-1]:
            i.directions[1][1] = None

        # right edge
        for i in maze:
            i[-1].directions[0][1] = None

        maze[0][0].end = True
        maze[0][0].directions = [[None, False], [None, False]]
        # maze[-1][-1].directions = [[False, None], [False, None]]
        maze[-1][-1].start = True
        return maze

    def change(self, seed=None):
        if seed is None:
            seed = random.randint(-sys.maxsize, sys.maxsize)
        random.seed(seed)

        x, y = random.randint(0, 1), random.randint(0, 1)
        while self.maze[self.origin[1]][self.origin[0]].directions[x][y] is None:
            x, y = random.randint(0, 1), random.randint(0, 1)
        self.maze[self.origin[1]][self.origin[0]].directions[x][y] = True
        # print(x, y)
        # print(self.maze[self.origin[0]][self.origin[1]])
        # print(self.origin)
        match (x, y):
            case (0, 0):
                self.origin = [self.origin[0]- 1, self.origin[1]]
            case (0, 1):
                self.origin = [self.origin[0]+ 1, self.origin[1]]
            case (1, 0):
                self.origin = [self.origin[0], self.origin[1]-1]
            case (1, 1):
                self.origin = [self.origin[0], self.origin[1]+1]
        for i in range(2):
            for j in range(2):
                if self.maze[self.origin[1]][self.origin[0]].directions[i][j] is not None:
                    self.maze[self.origin[1]][self.origin[0]].directions[i][j] = False
            # [[False, False], [False, False]]
        # for i in self.maze:
        #     print(i)
        # print(self.origin)
        # print(self.maze[self.origin[1]][self.origin[0]])
        # print("-" * 20)

    def fully_random(self, seed=None):
        if seed is None:
            seed = random.randint(-sys.maxsize, sys.maxsize)
        req_seed = seed
        for _ in range(100):
            self.change(seed)
            seed += 1
        return req_seed

if __name__ == "__main__":
    m = Maze()
    m.fully_random()
    # m.change(seed=0)
    # for _ in range(50):
    #     m.change()
    # print(m.maze)
