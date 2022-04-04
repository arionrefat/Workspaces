import re

fileIn = open("input.txt")

inputFile = fileIn.read().split()
inputFile = list(inputFile)

n  = int(inputFile[0])

regex = inputFile[1:n+1]
results = inputFile[n+2::]



for i in results:
  bool = False
  for j in regex:
    matched = re.fullmatch(j, i)
    
    if matched != None:
      print("YES", regex.index(j) + 1)
      bool = True
      
  if bool == False:
      print('NO', 0)