matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = list(map(list, zip(*matrix)))
print(transposed)
print(matrix)
print(*matrix)
#print(zip(*matrix))
print(list(zip(*matrix)))
#print(map(list, zip(*matrix)))  
