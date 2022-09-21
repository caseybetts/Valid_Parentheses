#Given a string containing '(',')','[',']','{' and/or '}' the output is True if the combinations are valid and False if they are not
from sys import argv
str = argv

# main function
def runFunction(s):

    # Turn the given string into a list
    targetList = list(s)

    # A string of length 1 or 0 is not valid
    if len(targetList) < 2: return False

    # Given the list of charactiers, t, and the kind of symbol to check, kind (1=(), 2={}, 3=[])
    # will return True if the string is valid for the given kind of symbol, otherwise False
    def checkit(t,kind):

        # recursive end point, given an empty list
        if len(t) == 0: return True

        # Return False if the number of opening and closing symbols is not equal
        if t.count(")") != t.count("("): return False
        if t.count("]") != t.count("["): return False
        if t.count("}") != t.count("{"): return False

        # Set 'start' and 'end' variables based on the 'kind' flag
        if kind == 1:
            end = ")"
            start = "("
        elif kind == 2:
            end = "}"
            start = "{"
        elif kind == 3:
            end = "]"
            start = "["

        # While there is a closing symbol
        while t.count(end) != 0:
            # Find the first closing symbol
            i = t.index(end)

            # If there is an opening symbol before the first closing symbol
            # work backwards from the first closing symbol to find the cooresponding opening symbol.
            # Replace the opening and closing symbol with 0 and 1, othewise return False
            if t[:i].count(start):
                j = i - 1

                while t[j] != start:
                    j-=1

                t[i] = 1
                t[j] = 0
            else: return False

            # If there is still a closing symbol, recursivly run this function on the smaller subset of the list for each symbol type
            if t.count(")"):
                if not checkit(t[j+1:i],1): return False
            if t.count("]"):
                if not checkit(t[j+1:i],2): return False
            if t.count("}"):
                if not checkit(t[j+1:i],3): return False

        # If no invalid characters were found
        return True

    # Run the check on the whole list for each symbol type
    if not checkit(targetList,1): return False
    if not checkit(targetList,2): return False
    if not checkit(targetList,3): return False

    # If no invalid characters were found
    return True

# Print the results of the function with the given input string
print(runFunction(str[1]))
