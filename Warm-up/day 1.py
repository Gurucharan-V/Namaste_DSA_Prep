# Write a program that defines a function to calculate the sum of two integers and prints the result. Call this function by passing two integer values.

# Explanation
# sum(a, b) is a function that takes two arguments.
# It adds them and stores the result in a variable named add.
# It then prints the result.
# sum(x, y) calls the function with x = 10 and y = 20, so it prints 30.
# Dry Run
# Input: a = 10, b = 20

# Step 1: add = 10 + 20 = 30

# Step 2: Print 30



def add(a,b):
    print(a+b)
    
add(2,4)


# Question
# Write a function that takes an integer and returns its square. Call this function and print the result.

# square(x) is a function that computes the square of a number.

# It returns the result instead of printing it.

# square(3) returns 9, which is then printed.

# Examples
# Input: 3 – Output: 9
# Input: 5 – Output: 25
# Input: 10 – Output: 100
# Approach
# To calculate the square of a number, follow these steps:

# Accept the input integer x.
# Multiply x by itself to get the square.
# Return the result from the function.
# Call the function with the desired number and print the returned value.


def Square(a):
     print(a*a)
    
Square(12)

# Question
# Write a function that accepts a person’s age and prints whether the person is:

# “Invalid input” if the age is less than 1.
# “Not eligible to vote” if the age is less than 18.
# “Eligible to vote” if the age is 18 or above.
# Call the function with different test values: 18, 0, and 8.

# Approach
# To solve this problem, follow these steps:

# Accept the input age in the function.
# Check if the age is less than 1; if yes, print “Invalid input”.
# If the age is valid but less than 18, print “Not eligible to vote”.
# If the age is 18 or more, print “Eligible to vote”.
# Test the function with various inputs to ensure all cases work correctly.
# Examples
# eligibleToVote(18) prints Eligible to vote
# eligibleToVote(0) prints Invalid input
# eligibleToVote(8) prints Not eligible to vote

def vote(n):
    if n < 1:
        print("Invalid input")
    elif n < 18:
        print('Not eligible to vote')
    else:
        print("Eligible to vote")
    
vote(18)
vote(0)
vote(8)


# Question
# Write a function that accepts a number and checks whether it is even or odd.

# If the number is divisible by 2 (i.e., remainder is 0), it’s an Even number.

# Otherwise, it’s an Odd number.

# Test the function with inputs 18 and 5.

# Approach
# Accept the input number in the function.
# Check if the number modulo 2 equals 0.
# If yes, print or return “Even”.
# Otherwise, print or return “Odd”.
# Test the function with different numbers to verify correctness.
# Example
# Input: 18
# Output: Even

# Input: 5
# Output: Odd


def checks_whether_it_is_even_or_odd(n):
    if n%2 ==0:
        print("even")
    else:
        print("odd")
        
checks_whether_it_is_even_or_odd(19)
