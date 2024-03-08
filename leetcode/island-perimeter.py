class Solution(object):
    # RUTENETT
    def islandPerimeter(self, grid):
        self.size = len(grid), len(grid[0])
        startnode = self.fill_with_nodes(grid)
        self.havkanter = 0
        self.DFS_recursive(grid, startnode, [])
    
    def gyldig_cords(self, cord):
        if cord[0] > self.size[0] or cord[1] > self.size[1] or cord[0] < 0 or cord[1] < 0:
            return False
        return True


    def fill_with_nodes(self, grid):
        startnode = None
        for y, i in enumerate(grid):
            for x, j in enumerate(i):

                if j == 1:
                    j = Node(y,x)
                    if startnode == None:
                        startnode = j

        return startnode
    

    def DFS_recursive(self, node, visited):
        visited.append(node)


class Node:
    def __init__(self, y, x):
        self.cords = [y, x]
        self.nswe = self.finn_naboer()
    
    def finn_naboer(self):
        cords = self.cords
        unsafe_cords = []
        unsafe_cords.append([cords[0] - 1, cords[1]])
        unsafe_cords.append([cords[0] + 1, cords[1]])
        unsafe_cords.append([cords[0], cords[1] - 1])
        unsafe_cords.append([cords[0], cords[1] + 1])

    
