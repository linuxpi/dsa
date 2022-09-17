"""
Give a city map with people, trees, walls. Find the shortest walkable distance for every person to the closest tree.
Input:
O -> People
T -> Tree
X -> Wall

O 0 O T X
O X X O T
O O O O O
T X X X O
O O T O O
O X X T O

{index: 3}

[0 ]

[0 0]
[0 X X 0]
[0 X T 0]

[0 0 | 0 X X 0 | ]
 
O T O O X
O X X O T
O O O O O
O X X X O
O O T O O
O X X T O
 
Output :
 
1 0 1 2 -1
2 -1 -1 1 0
3 4 3 2 1
3 -1 -1 -1 2
2 1 0 1 2
3 -1 -1 0 1
 
"""

from Queue import Queue

def find_distance(matrix):
    if not matrix or not matrix[0]:
        return matrix

    q = Queue()
    maxLength = len(matrix)
    maxBreadth = len(matrix[0])

    result = [[-1 for _ in range(maxBreadth)] for _ in range(maxLength)]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i]))
            if matrix[i][j] == 'T':
                result[i][j] = 0
                nearestPeople = getNN(matrix, i, j)
                [q.push(p) for p in nearestPeople]
    
    q.push("|")
    distance = 1
    while(not q.is_empty()):
        value = q.pop()
        if (value == '|'):
            distance += 1
            q.push("|")
            continue
        
        i, j = value
        
        if (result[i][j] == -1 or result[i][j] > distance):
            result[i][j] = distance
        
        nearestPeople = getNN(matrix, i ,j)
        [q.push(p) for p in nearestPeople]
        
    return result


def getNN(matrix, i, j):
    children = []
    maxLength = len(matrix)
    maxBreadth = len(matrix[0])
    
    if (i+1 < maxLength and matrix[i+1][j] == '0'):
        children.append((i+1, j))
        
    if (j+1 < maxBreadth and matrix[i][j+1] == '0'):
        children.append((i, j+1))
    
    if (i-1 >= 0 and matrix[i-1][j] == '0'):
        children.append((i-1, j))
        
    if (j-1 >= 0 and matrix[i][j-1] == '0'):
        children.append((i, j-1))
        
    return children

