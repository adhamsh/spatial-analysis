from dijkstra import *

#We represent the closed nodes with a list of previous nodes.
#Each iteration has a condidate node with the smallest distance removed
#starting at function get_remove_min. And then where it
#says for v in u it then becames represented in the previous node
#list.

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

s_test = shortest_path(3,6,distance_matrix)


print('Vertices and total distance for dijkstra are: ',s_test)

#Results:
#([6, 4, 1, 0, 3], 22)
