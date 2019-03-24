dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 东南西北


def mark(maze, pos):
    # 给迷宫maze的位置pos标2表示“到过了”
    maze[pos[0]][pos[1]] = 2


def passable(maze, pos):
    # 检查迷宫maze的位置pos是否可行
    return maze[pos[0]][pos[1]] == 0


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ")
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                print(pos, end=" ")
                return True
    return False

