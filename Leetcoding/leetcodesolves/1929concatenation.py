from typing import List

def getConcatenation(nums: List[int]) -> List[int]:
    # return nums + nums # this is the easy way to do it
    anotherList = nums.copy()

    for i in nums:
        anotherList.append(i)

    return anotherList


print(getConcatenation([1, 3, 2, 1]))

# the time complexity is O(n) and the space complexity is O(n) 
# because we are creating a new list and copying the elements of the original list into it