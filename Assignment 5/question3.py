#Started Question 3 - Dec 7th 2020 (11:10am)

import maze_helper as mh

#depth-first search - Dec 7th 2020 (12:13pm)
def dfs(maze, position, explored=[]):
    if len(maze[0])*2 == len(explored):
        return None
    else:
        explored.append(position)
        mh.add_walk_symbol(maze, position)
        adj_pos = mh.get_adjacent_positions(maze, position)
        for adj_point in adj_pos:
            if adj_point not in explored:
                dfs(maze, adj_point, explored)

#find start of the maze - Dec 7th 2020 (12:21pm)
def findstart(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (maze[y][x] == "O"):
                return x, y + 1
    return -1, -1

if __name__ == "__main__":
    print("Here is the maze before solving:")
    maze = mh.sample_maze()
    mh.print_maze(maze)

    #starting with (5, 1) sinces its below the origin/starting point
    x, y = findstart(maze)
    if(x != -1 and y != -1):
        dfs(maze, (x, y))
        
        print("Here is the solved maze:")
        mh.print_maze(maze)

    else:
        print("Could not find a starting point...")

#finished question 3 - Dec 7th 2020 (12:27pm)