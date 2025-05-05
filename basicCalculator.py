# Time Complexity : O(2n)
# Space Complexity : O(n)

# Approach:
# 1. Initialize a stack to keep track of numbers and signs.
# 2. Iterate through the string:
#    - If the character is a digit, build the current number.
#    - If the character is an operator or the end of the string, process the current number based on the last sign.
#    - If the character is '(', push the sign onto the stack, along with a marker for the start of a new expression.
#    - If the character is ')', pop from the stack until the marker is found, and apply the sign.
# This handles nested parentheses.
# 3. Finally, sum up the remaining numbers in the stack to get the result.
class Solution:
    def calculate(self, s: str) -> int:
        # Remove all spaces from the string
        s = s.strip()
        # Initialize a stack to keep track of numbers and signs
        stack = []
        # Initialize current number and last sign
        currNum = 0
        lastSign = '+'
        # Iterate through the string
        for i in range(len(s)):
            # If the character is a digit, build the current number
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
            # If the character is an operator or the end of the string
            # process the current number based on the last sign
            if (not s[i].isdigit() and s[i] != ' ' and s[i] != '(' and s[i] != ')') or (i == len(s)-1):
                # If the last sign is '+', push the current number onto the stack
                if lastSign == '+':
                    stack.append(currNum)
                # If the last sign is '-', push the negative of the current number onto the stack
                elif lastSign == '-':
                    stack.append(-currNum)
                # Reset the current number
                currNum = 0
                # Update the last sign to the current character
                lastSign = s[i]
            # If the character is '(', push the sign onto the stack
            if s[i] == '(':
                # Push the last sign onto the stack
                if lastSign == '-': stack.append(-1)
                else: stack.append(1)
                # Push a marker for the start of a new expression
                stack.append(float('inf'))
                # Reset the current number and last sign
                currNum = 0
                lastSign = '+'
            # If the character is ')', pop from the stack until the marker is found
            elif s[i] == ')':
                if lastSign == '-': currNum *= -1
                # Pop from the stack until the marker is found
                while stack[-1] != float('inf'):
                    # Keep adding the popped numbers to the current number
                    currNum += stack.pop()
                # Pop the marker
                stack.pop()
                # Pop the sign from the stack
                stack.append(currNum * stack.pop())
                # Reset the current number and last sign
                currNum = 0
                lastSign = '+'
        # If there are any remaining numbers in the stack, add them to the current number
        while stack:
            currNum += stack.pop()
        # Return the final result
        return currNum