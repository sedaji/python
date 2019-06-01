tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

L = [0,0,0] 
for i in range(3): 
  for j in range(4): 
      listLen = len(tableData[i][j]) if L[i] < listLen: L[i] = listLen

def printTable(): 
  for i in range(4): 
    for j in range(3): 
      print((tableData[j][i]).rjust(L[j]+2,'.'), end=' ') print()
printTable()
