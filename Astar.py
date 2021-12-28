import math
#this is a heuritic list where it stores the value of heuristic i.e manhanttan distance from given node to goal node
#intially it is taken asa zero for reference
heuristic = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]
class Node():
    def __init__(self, heuristic,parent=None, position=None):
        #parent is optional as start node dont have a parent

        self.parent = parent
        self.position = position
        self.g = 0
        #hueristic list has values of heuristic pre computed using the function findheuristic
        self.h = heuristic[position[0]][position[1]]
        self.f = self.g+self.h
    def __eq__(self, other):
        return self.position == other.position


#this function findheuristic is function where we find the heuristic function from given node to goal node using manhattan distance
def findheuristic(heuristic, node, goal):
    x = node[0]
    y = node[1]
    k = abs(x - goal[0]) + abs(y - goal[1])
    heuristic[x][y] = math.floor((k))


#this is the function to calcuate astar search algorithm which take maze, start node ,end node, and heuristic function
def astar(maze, start, goal,heuristic):
    start_node = Node(heuristic,None,start)
    end_node = Node(heuristic,None, goal)
#The OPEN list keeps track of those nodes that need to be examined.
# The CLOSED list keeps track of nodes that have already been examined
    open_list = []
    closed_list = []
#intially we examine the start node
    open_list.append(start_node)
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        #this for loop is to find the next node which has less f value
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        #we have searched the node so we pop it from open and add to close
        closed_list.append(current_node)
        #check for end case
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                #we keep backtrack using the parent
                path.append(current.position)
                current = current.parent
            return path[::-1]
        children = []
        #here we are finding a path and we either move left or right or top or down

        for np in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            #so now we check whether those cell is in maze or not
            node_position = (current_node.position[0] + np[0], current_node.position[1] + np[1])
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue
            #if cell value is 1 we dont reuqire that cell as it is blocked/wall
            if maze[node_position[0]][node_position[1]] != 0:
                continue
           #we have got a new node or we can say we explored a new node so we add it to children list
            new_node = Node(heuristic,current_node, node_position)
            children.append(new_node)
        for child in children:
            for cc in closed_list:
                #here if we have already explored the node we can leave that
                if child == cc:
                    continue
            child.g = current_node.g + 1
            #as we move cell one by one i assumed cost as one unit per move
            child.f = child.g + child.f
            #here child.f is added to child.g , here heurstic is already added to the node in its constructor itself refer line 16
            for on in open_list:
                if child == on and child.g > on.g:
                    continue
            open_list.append(child)
def main():
    maze = [[0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0]]
    start = (1, 0)
    end = (4, 5)
    row = len(heuristic)
    col = len(heuristic[0])
    for i in range(0, row):
        for j in range(0, col):
            findheuristic(heuristic, [i, j], end)
    path = astar(maze, start, end,heuristic)
    print(path)

if __name__ == '__main__':
    main()