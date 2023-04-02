from stack import Stack

"""
Iterative implementation to check palindromes in a string using a stack data structure
"""
def is_palindrome(string):
    stack = Stack() # Initialize an instance of stack
    n = len(string)
    
    # Loop through the first half of the string elements & add elements from the string into stack
    for i in string[:n//2]:
        stack.push(i)

    if n%2 != 0: mid = (n//2) + 1   # Set midpoint for odd string length
    else: mid = n//2    # Set midpoint for even string length
    
    # Returns false if any of the string characters dont match up with their respective element in stack
    for i in range(mid, n):
        if string[i] == stack.pop(): pass
        else: return False

    return True # Returns true if all elements in stack matchup perfectly with the string


def testPalindrome():
    print(is_palindrome("level"))
    print(is_palindrome("lever"))
    print(is_palindrome("definitelynotapalindrome"))
    print(is_palindrome("ablewasiereisawelba"))
    print(is_palindrome("ablewasiereisawelbar"))


if __name__ == "__main__":
    testPalindrome()