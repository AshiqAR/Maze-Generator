import random

def getNeighbours(n,parent,r,c):
    li = []
    if n%c!=0 and (find(parent,n)) != (find(parent,n-1)):
        li.append(n-1)
    if n//c!=0 and (find(parent,n)) != (find(parent,n-c)):
        li.append(n-c)
    if n%c!=c-1 and (find(parent,n)) != (find(parent,n+1)):
        li.append(n+1)
    if n//c < r-1 and (find(parent,n)) != (find(parent,n+c)):
        li.append(n+c)
    return li
    
def generateMaze(r,c):
    parent = makeSet(r,c)
    edge = []
    
    while (find(parent,0) != find(parent,(r*c)-1)):
        rand1 = random.choice(parent)
        neighbours = getNeighbours(rand1,parent,r,c)
        if neighbours==[]:
            continue
        rand2 = random.choice(neighbours)
        # print("selected edge",rand1,rand2)
        parent = union(parent, rand1,rand2)
        # print("parent",parent)
        edge.append({rand1,rand2})
        # print("Edges",edge)
        # print()
    edge.sort()
    return edge

def makeSet(r,c):
    parent = [i for i in range(r*c)]
    return parent

def find(parent,n):
    if(parent[n]!=n):
        parent[n] = find(parent,parent[n])
    return parent[n]

def union(parent,n1,n2):
    r1 = find(parent,n1)
    r2 = find(parent,n2)
    if r1 != r2:
        parent[r2] = r1
    return parent


