# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def main(haystack, k):
    # sort the list
    haystack.sort()
    length = len(haystack)

    for i in range(length):
        if i > k:
            break
        for j in range(length):
            if i == j:
                continue

            if j > k:
                break

            if haystack[i] + haystack[j] == k:
                return True

    return False
