def getAdjacent(edgeList,src):
    li = []
    for ele in edgeList:
        if src in ele:
            li.append(ele)
    return li

def isReachable(edgeList,path,src,dest,visited,initial={0}):
    visited.append(initial)
    path.append(initial)
    if src == dest:
        return True,path
    li = getAdjacent(edgeList,src)
    for ele in li:
        if ele not in visited:
            reach, path = isReachable(edgeList,path,int(next(iter(ele-{src}))),dest,visited,ele)
            if reach:
                return True,path   
    path.pop()
    return False,path

def getZero(edgeList):
    li = []
    for ele in edgeList:
        if 0 in ele:
            li.append(ele)
    return li


def readMaze():
    edgeList = []
    with open("Generated_maze.txt") as f:
        array_str = f.readline().strip()
        r = int(f.readline())
        c = int(f.readline())
    edgeList = eval(array_str)
    return edgeList,r,c


edgeList,r,c = readMaze()
print("Number of rows in the maze is: ",r)
print("Number of columns in the maze is: ",c)
print("Edge list of the maze is: ")
print(edgeList)
path = []
visited = []
src = 0
dest = r*c-1
reachable,path = isReachable(edgeList,path,src,dest,visited)
path.remove({0})
print("\nPath obtained from start to the last cell is:")
print(path)
