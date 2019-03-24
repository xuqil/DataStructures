import random


def createMaze(n):
    maze = [([0] * n) for i in range(n)]  # 初始化一个n阶二维数组
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:  # 迷宫周围设障碍
                maze[i][j] = "*"
            else:
                rate = 0.7  # 设置非障碍的概率
                if random.random() > rate:
                    maze[i][j] = "*"
    return maze


def createStart(maze):
    for i in range(1, len(maze) - 1):  # 从左上角开始寻找，若为非障碍则为起点
        for j in range(1, len(maze[i]) - 1):
            if maze[i][j] == 0:
                new_start = [i, j]
                print("起点：", new_start)
                return new_start


def createEnd(maze):
    for i in range(len(maze) - 1, 1, -1):  # 从右下角开始寻找，若为非障碍则为终点
        for j in range(len(maze[i]) - 1, 1, -1):
            if maze[i][j] == 0:
                new_end = [i, j]
                print("终点：", new_end)
                return new_end


def nextNode(maze, road, i):
    if i == 1:
        a = road[-1][0]  # 往右走的坐标
        b = road[-1][1] + 1
        if maze[a][b] != "*":
            return [a, b]
        return None
    if i == 2:
        a = road[-1][0] + 1  # 往下走的坐标
        b = road[-1][1]
        if maze[a][b] != "*":
            return [a, b]
        return None
    if i == 3:
        a = road[-1][0]  # 往左走的坐标
        b = road[-1][1] - 1
        if maze[a][b] != "*":
            return [a, b]
        return None
    if i == 4:
        a = road[-1][0] - 1  # 往上走的坐标
        b = road[-1][1]
        if maze[a][b] != "*":
            return [a, b]
        return None


def is_old(next_node, oldlist):  # 判断该点是否走过（改进版 ）
    for i in range(len(oldlist)):
        if next_node == oldlist[i]:
            return 0
    return 1


def is_old2(next_node, the_road):  # 判断该点是否走过
    if len(the_road) > 2 and next_node == the_road[-2]:
        return 0
    return 1


def findRoad(maze, begin, stop):
    road = []  # 将road作为栈,road[-1]代表栈顶
    old_road = []
    road.append(begin)  # 将起点入栈
    old_road.append(begin)
    # if nextNode(maze,road)==None:#判断起点是否是孤立点
    #     return None
    # road.append(nextNode(maze, road))
    while road != []:
        if road[-1] == stop:
            return road
        tag = 1  # 判断标识
        while tag != 5:
            next_node = nextNode(maze, road, tag)  # 寻找下一个点
            if next_node == None or is_old(next_node, old_road) == 0:  # 若下一点走过了或要碰壁了尝试别的方向
                tag += 1
            else:
                road.append(next_node)
                old_road.append(next_node)
                tag = 1
                break
        if tag == 5:  # 若路都不通，栈顶元素抛出
            a = road[-1][0]
            b = road[-1][1]
            maze[a][b] = "*"
            road.pop(-1)
    # next_node=nextNode(maze,road)#寻找下一个点
    # if next_node == road[-2]:
    #     road.pop(-1)
    # else:
    #     road.append(next_node)
    return road


def printMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], " ", end="")
        print("")


if __name__ == "__main__":  # 注意：本程序设置的size是除去外围障碍的阶数
    size = 10
    new_maze = createMaze(size + 2)  # 创建迷宫
    printMaze(new_maze)  # 打印迷宫
    start = createStart(new_maze)  # 定义起点
    end = createEnd(new_maze)  # 定义终点
    the_road = findRoad(new_maze, start, end)  # 寻找出路
    if the_road == []:
        print("无路可走")
    else:
        print(the_road)
