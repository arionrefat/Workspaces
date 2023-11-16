def isAnagram(s: str, t: str) -> bool:
    sorteds_string = sorted(s)
    sortedt_string = sorted(t)

    return sorteds_string == sortedt_string


# the time complexity for the above O(nlogn)
# because of the sorting algorithm
# the space complexity for the above O(1) because we are not using any extra space


def isAnagramHashTable(s: str, t: str) -> bool:
    # return Counter(s) == Counter(t) # slightly faster

    if len(t) != len(s):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countS.get(t[i], 0)

    for c in countS:
        print(c)

        if countS[c] != countT.get(c, 0):
            return False

    return True


print(isAnagramHashTable("anagram", "aaangram"))

# the time complexity for the above O(n) because we are iterating over the string
# the space complexity for the above O(1) because we are not using any extra space
