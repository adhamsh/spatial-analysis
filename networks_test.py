
from bfs import *
from dfs import *

con = [ [0, 1, 3],
        [0, 3, 5],
        [1, 2, 11],
        [1, 4, 9],
        [2, 5, 3],
        [2, 3, 8],
        [3, 7, 15],
        [4, 5, 6],
        [4, 6, 5],       
        [5, 7, 12],       
        [6, 7, 11] ]
# get the number of nodes

n = 0

for row in con:
    if row[0] > n:
        n = row[0]
    if row[1] > n:
        n = row[1]



n = n + 1


# get distance matrix

INF = float('inf')

distance_matrix = [ [INF] * n for i in range(n)]

for row in con:
    i = row[0]
    j = row[1]
    d = row[2]
    distance_matrix[i][j] = d
    distance_matrix[j][i] = d


#get a adjacency list

networklist = [[] for i in range(n)]

for row in con:
    i = row[0]
    j = row[1]
    d = row[2]
    networklist[i].append(j)
    networklist[j].append(i)
    


bfs_test = bfs(networklist,2)
dfs_test = dfs(networklist,2)

print('Verticed for bfs: ',bfs_test)
print('Vertices for dfs: ',dfs_test)

#Results:
#Verticed for bfs:  [2, 1, 5, 3, 0, 4, 7, 6]
#Vertices for dfs:  [2, 3, 7, 6, 4, 0, 5, 1]
