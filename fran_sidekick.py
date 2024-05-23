# Jordi Becerril Enriquez
# May 21, 2024
# fan side kick project.


"""
- given two input strings determine and return/output 
the longest common Substring.

solution:
The way I solved this was by:

1. converting the input string(s) to arrays of all possible sub strings.
- I did this via two nested for loops. The first loop is like a column. And the second iterates like a row.
- "abcde" -> 
- ['a', 'ab', 'abc', 'abcd', 'abcde', 
   'b', 'bc', 'bcd', 'bcde', 
   'c', 'cd', 'cde', 
   'd', 'de', 
   'e']
- repeat for both input strings. 

2. Once we have all possible sub strings. We can now easily check them against each other to find any-
common sub strings and return the length.
- I used two nested loops and an if statment to check for equal sub strings.
- also keeping track of the len() and saving the largest we find.


Follow ups:
1. for subsequence I could solve by checking all possible subsequences, where we remove a character to create the subsequence.
2. To make the algorithm run more efficiently we could do eliminate itterating over duplicates.
    - we could do this by storing the sub strings in a hash map.
    - this would also reduce time complexity and improve efficiency for loop up instead of loop up with two nested loops.
3. Time and space complexity I think would be O(n^2 * n^2) = O(n^4). 
"""


def main(string_one, string_two):
    # initialize our values
    one = []
    two = []
    largest_len_substring = 0
    substring = ""

    # helper function returns an array of substrings, so we can find common sub strings easily
    one = collect_substrings(string_one)
    two = collect_substrings(string_two)

    # find and return the largest sub string and it's len
    largest_len_substring, substring = get_largest_substring(one, two)

    print(
        'largest substring is: "'
        + str(substring)
        + '" with len of: '
        + str(largest_len_substring)
    )


# helper functions


# function to convert our string into an array of substrings
def collect_substrings(string):
    sub_array = []
    sub_string = ""

    # loop through string to create an array of sub strings
    for i in range(len(string)):
        # each char is a sub string.
        # we are creating a sub string of all possibilities withing the string.
        # then we add the sub string to an array.
        sub_string += string[i]
        sub_array.append(sub_string)

        # nested for loop makes it easy to create all sub string possibilities
        # python syntax: (start, stop, step)
        for j in range(i + 1, len(string), 1):
            # create the sub string and add it to the array.
            sub_string += string[j]
            sub_array.append(sub_string)

        sub_string = ""

    return sub_array


# function to compare two arrays of strings to find the largest commone sub string.
def get_largest_substring(one, two):
    num = 0
    substring = ""

    for i in range(len(one)):
        for j in range(len(two)):
            # check to see if we found a common sub string.
            # and save the largest one we find.
            if one[i] == two[j] and len(one[i]) > num:
                num = len(one[i])
                substring = one[i]

    return num, substring


string_one = "abcde"
string_two = "aabc"

# string_one = "this is an original"
# string_two = "i am original today"

main(string_one, string_two)
