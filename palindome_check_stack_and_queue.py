from collections import deque

def check_palindrome(user_input):
    """
    This function checks if the given input text is a palindrome.
    Returns True if it is a palindrome and False if it's not.
    """

    # normalizing input
    normalized_input = ''.join(char.lower() for char in str(user_input) if char.isalnum())
    length = len(normalized_input)

    # define stack and queue sizes
    stack_size = length // 2  # half size rounded down
    queue_size = (length + 1) // 2  # half size rounded up

    stack = deque()
    queue = deque()

    #populating stack
    for i in range(stack_size):
        stack.append(normalized_input[i])

    # populating queue
    for i in range(length - queue_size, length):
        queue.append(normalized_input[i])

    # handle cases with odd length where middle character does not affect the palindrome check
    if len(queue) > len(stack):
        queue.popleft() #omit the first character

    # compare characters in stack & queue
    for char in range(len(queue)):
        if stack.pop() != queue.popleft():
            return False

    return True

print("This program checks if your input is a palindrome!")
user_input = input("Please enter your text:")

if check_palindrome(user_input) == True:
    print("Your text is a palindrome.")
else:
    print("Your text is not a palindrome.")