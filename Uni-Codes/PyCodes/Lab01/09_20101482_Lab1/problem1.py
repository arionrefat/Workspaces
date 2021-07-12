fileIn = open("input.txt")
fileOut = open("output.txt", "w")
fileRecord = open("record.txt", "w")

inputFile = fileIn.read().split()
inputFile = list(inputFile)

integers = [x for x in inputFile if not x.isalpha()]
strings = [x for x in inputFile if x.isalpha()]

palindromeCount = 0
evenParityCount = 0
oddParityCount = 0
noParityCount = 0
noPalindrome = 0
totalRecord = len(inputFile) // 2

def isPalindrome(string):
    global palindromeCount, noPalindrome
    if string == string[::-1]:
        palindromeCount += 1
        return "a"
    else:
        noPalindrome += 1
        return "not a"

def isParity(number):
    global evenParityCount, oddParityCount, noParityCount
    number = float(number)

    if number % 1 == 0:
        if number % 2 == 0:
            evenParityCount += 1
            return "has even"
        else:
            oddParityCount += 1
            return "has odd"
    else:
        noParityCount += 1
        return "cannot"


for i in range(totalRecord):
    print(f"{integers[i]} {isParity(integers[i])} parity and {strings[i]} is {isPalindrome(strings[i])} palindrome",
          file=fileOut)

print(f"Percentage of odd parity: {int((oddParityCount / totalRecord) * 100)}%", file=fileRecord)
print(f"Percentage of even parity: {int((evenParityCount / totalRecord) * 100)}%", file=fileRecord)
print(f"Percentage of no parity: {int((noParityCount / totalRecord) * 100)}%", file=fileRecord)
print(f"Percentage of Palindrome: {int((palindromeCount / totalRecord) * 100)}%", file=fileRecord)
print(f"Percentage of no Palindrome: {int((noPalindrome / totalRecord) * 100)}%", file=fileRecord)

fileOut.close()
fileRecord.close()
fileIn.close()