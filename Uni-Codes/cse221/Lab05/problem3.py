fileInput = open("input3.txt")
fileoutput = open("output3.txt", "w")
disposable = fileInput.readline()
workingHours = list(map(int,fileInput.readline().strip('\n').split(' ')))
workingHours.sort()
string = fileInput.readline()

sequence = ''
stack = []
index = 0
jackHours = 0
jillHours = 0

for c in string:
    if c == "J":
        stack.append(workingHours[index])
        jackHours += workingHours[index]
        sequence += str(workingHours[index])
        index += 1
    
    elif c == "j":
        val = stack.pop()
        sequence += str(val)
        jillHours += val
        
print(sequence, file=fileoutput)
print(f"Jack will work for {jackHours} hours", end = '\n', file = fileoutput)
print(f"Jill will work for {jillHours} hours", end = '\n', file = fileoutput)