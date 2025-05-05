# Time Complexity : O(n)
# Space Complexity : O(n)

# Approach:
# 1. Initialize a stack to keep track of numbers and signs.
# 2. Iterate through the string:
#    - If the character is a digit, build the current number.
#    - If the character is an operator or the end of the string, add the current number to the stack based on the last sign.
#    - If the last sign is '*', or '/', pop the last number from the stack and perform the operation with the current number, and push the result back to the stack.
#    - If the last sign is '+', or '-', push the current number to the stack.
# 3. Finally, sum up the numbers in the stack to get the result.
class Solution:
    def calculate(self, s: str) -> int:
        # Initialize a stack to keep track of numbers and signs
        stack = []
        # Remove all spaces from the string
        s = s.strip()
        # Initialize current number and last sign
        currNum = 0
        lastSign = '+'
        # Iterate through the string
        for i in range(len(s)):
            # If the character is a digit, build the current number
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
            # If the character is an operator or the end of the string process the current number based on the last sign
            if not s[i].isdigit() and s[i] != ' ' or i == len(s)-1:
                # If the last sign is '+', push the current number onto the stack
                if lastSign == '+':
                    stack.append(currNum)
                # If the last sign is '-', push the negative of the current number onto the stack
                elif lastSign == '-':
                    stack.append(-currNum)
                else:
                    # If the last sign is '*', pop the last number from the stack and multiply it with the current number
                    num = stack.pop()
                    if lastSign == '*':
                        currNum = currNum * num
                    # If the last sign is '/', pop the last number from the stack and divide it by the current number
                    # Check the sign of the last number
                    # If the last number is negative, multiply the result by -1
                    elif lastSign == '/':
                        sign = num<0
                        currNum = abs(num) // currNum
                        if sign:
                            currNum *= -1
                    # Push the result back to the stack
                    stack.append(currNum)
                # Reset the current number
                currNum = 0
                # Update the last sign to the current character
                lastSign = s[i]
        # Sum up the numbers in the stack to get the result 
        while stack:
            currNum += stack.pop()
        # Return the calculated value
        return currNum
    
# Time Complexity : O(n)
# Space Complexity : O(1)

# Approach:
# 1. Initialize variables to keep track of the current number, last sign, calculated value so far, and tail.
# 2. Iterate through the string:
#   - If the character is a digit, build the current number.
#   - If the character is an operator or the end of the string, process the current number based on the last sign.
#   - If the last sign is '+', add the current number to the calculated value and update the tail.
#   - If the last sign is '-', subtract the current number from the calculated value and update the tail.
#   - If the last sign is '*', subtract the tail from the calculated value, multiply the tail with the current number, and add it to the calculated value.
#   - If the last sign is '/', check the sign of the tail, divide the absolute value of the tail by the current number, and update the calculated value and tail accordingly.
# 3. Finally, return the calculated value.
class Solution:
    def calculate(self, s: str) -> int:
        # Remove all spaces from the string
        s = s.strip()
        # Initialize current number, last sign, calculated value, and tail
        currNum = 0
        lastSign = '+'
        calc = 0
        tail = 0
        # Iterate through the string
        for i in range(len(s)):
            # If the character is a digit, build the current number
            if s[i].isdigit():
                currNum = currNum * 10 + int(s[i])
            # If the character is an operator or the end of the string process the current number based on the last sign
            if not s[i].isdigit() and s[i] != ' ' or i == len(s)-1:
                # If the last sign is '+', add the current number to the calculated value and update the tail
                if lastSign == '+':
                    calc = calc + currNum
                    tail = currNum
                # If the last sign is '-', subtract the current number from the calculated value and update the tail
                elif lastSign == '-':
                    calc = calc - currNum
                    tail = -currNum
                else:
                    # If the last sign is '*', subtract the tail from the calculated value, multiply the tail with the current number, and add it to the calculated value
                    if lastSign == '*':
                        calc = (calc - tail) + (tail * currNum)
                        tail = tail * currNum
                    # If the last sign is '/', check the sign of the tail, divide the absolute value of the tail by the current number, and update the calculated value and tail accordingly
                    elif lastSign == '/':
                        sign = tail<0
                        tmp = (abs(tail)//currNum)
                        if sign:
                            tmp *= -1
                        calc = (calc - tail) + tmp
                        tail = tmp
                # Update the last sign to the current character
                lastSign = s[i]
                # Reset the current number
                currNum = 0
        # Return the calculated value
        return calc