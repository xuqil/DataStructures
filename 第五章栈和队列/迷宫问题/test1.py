def createMaze(n):
    maze = [([0]*n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == n-1:
                maze[i][j] = "*"
    for i in range(n):
        print(maze[i])


createMaze(5)
