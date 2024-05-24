# Jordi Becerril Enriquez
# May 21, 2024
# fan side kick project.

"""
write up:
- to find the longest common subsequence we can use a recursive algorithm. 
- first we create our recursive function (longest_common_sub)

- and we check if either string lengeth is empty

- if the last chars of both strings are the same, we add 1 to the result of the 
function called on the remaning parts of the strings.

- if the last chars are different, the LCS is the maximum length obtained by
either exluding the last char of the first string (i - 1) or the second string (j - 1)

- I like to thing of recursion as a stack. ie, a call stack.
"""


def longest_common_sub(s_one, s_two, i, j):
    # check if our strings are empty.
    if i == 0 or j == 0:
        return 0
    # check if the last chars are the same. If true, the char is part of lcs
    elif s_one[i - 1] == s_two[j - 1]:
        # we add 1 and move to the next pair of chars.
        return 1 + longest_common_sub(s_one, s_two, i - 1, j - 1)
    # if the last chars are diff. we have two options.
    else:
        return max(
            # exclude the last char of the first string and find the lcs of the remaning parts
            longest_common_sub(s_one, s_two, i - 1, j),
            # exclude the last char of the second string and find the lcs of the remaining parts
            longest_common_sub(s_one, s_two, i, j - 1),
        )


s_one = "abcde"
s_two = "ace"

print(
    "Length is: ",
    longest_common_sub(s_one, s_two, len(s_one), len(s_two)),
)
