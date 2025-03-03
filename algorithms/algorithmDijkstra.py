class Point:
    def __init__(self):
        self.distance = 0
        self.minDist = 0
        self.visited = False
c = 6
graph = [[Point() for i in range(c)] for i in range(c)]

graph[0][1].distance = 7
graph[0][2].distance = 9
graph[0][5].distance = 14


graph[1][0].distance = 7
graph[1][2].distance = 10
graph[1][3].distance = 15


graph[2][0].distance = 9
graph[2][1].distance = 10
graph[2][3].distance = 11
graph[2][5].distance = 2


graph[3][1].distance = 15
graph[3][2].distance = 11
graph[3][4].distance = 6


graph[4][3].distance = 6
graph[4][5].distance = 9


graph[5][0].distance = 14
graph[5][2].distance = 2
graph[5][4].distance = 9

for l in graph:
    for col in l:
        print(f"{col.distance:2}", end=' ')
    print()


print('-'*18)

for i in range(c):
    pt0 = graph[i][i]
    for j in range(c - (i + 1)):
        pt1 = graph[i][j]
        if pt1.distance : continue
        if pt1.minDist == 0:
            pt1.minDist = pt1.distance
        else:
            pass            
    for pt in graph[i][i+1:c]:
        if pt.distance == 0:
            continue
        
        if pt.minDist == 0:
            pt.minDist = pt.distance
        else:
            t = pt.distance + pt0.minDist
            if pt.minDist > t:
                pt.minDist = t
      
                
for l in graph:
    for col in l:
        print(f"{col.minDist:2}", end=' ')
    print()   
