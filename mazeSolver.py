from rat_in_Maze import generateMaze

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

r = int(input("Enter number of rows in the maze: "))
c = int(input("Enter number of columns in the maze: "))

edgeList = generateMaze(r,c)
print("Edge list of the maze is: ")
print(edgeList)
path = []
visited = []
src = 0
dest = r*c-1
reachable,path = isReachable(edgeList,path,src,dest,visited)
path.sort()
# print("Path from source to destination is: ",path)
print("\npath")
print(path)

