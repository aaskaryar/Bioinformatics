# Aria Askaryar
# CPSC 485 M/W 11:30am

def edit_distance(s, t):
    """
    Created by Aria Askaryar
    Spring Semester 2022
    created with Python3 on PyCharm

        This program will edit the distance between two strings (words).

    This program is perferably to be run on PyCharm. Open the project then open the
    485project.py file and run the program. Once the program is ran it will tell you
    to enter one word then hit enter and enter another word. Once you enter both
    words and hit enter the edit distance between the two words will be calculated.

    how to use: Open this the "485project.py" file in any python idle, PyCharm is recommended,
    then save the file. Once saved run the  file. Once it is ran it will instruct you to enter
    one word then hit the enter key and enter a second word and hit enter again. Now the
    program will out put the edit distance between the two strings. Look below to see a
    few examples.

    output:
    >>> edit_distance("a", "a")
    0
    Enter first word then press enter:
    Enter second word:
    a
    a
    The Edit Distance is:
    0

    >>> edit_distance("short", "ports")
    3
    Enter first word then press enter:
    Enter second word:
    short
    ports
    The Edit Distance is:
    3
    >>> # Explanation: s h o r t −
    >>> #              − p o r t s
    >>> edit_distance("editing", "distance")
    5
    Enter first word then press enter:
    Enter second word:
    editing
    distance
    The Edit Distance is:
    5
    >>> # Explanation: e d i − t i n g −
    >>> #              − d i s t a n c e
    """

    len_s = len(s) + 1
    len_t = len(t) + 1

    # Create a distance matrix and write in initial values.
    d = [[x] + [0] * (len_t - 1) for x in range(len_s)]
    d[0] = [x for x in range(len_t)]

    for i in range(1, len_s):
        for j in range(1, len_t):

            # Levenshtein distance calculation.
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1]) + 1

    # The last element of the matrix is edit distance metric.
    print("The Edit Distance is: ")
    return d[-1][-1]


if __name__ == "__main__":
    print("Enter first word then press enter: ")
    print("Enter second word: ")
    print(edit_distance(input(), input()))
