m = [1,2,3,-1,-2,-3,-4,7,3,8]
arr = [9,12,23]


# Print a square pattern of stars (*) of size n x n.

# Example Output

# ****
# ****
# ****
# ****
# ****
# Approach

n=5

for x in range (n):
    print(" * "*n)

print("\n")
# Write a program to print a right-angled triangle of stars (*) with n rows.

# Example Output

# *
# **
# ***
# ****
  
  
for x in range(n):
    print(" *"*(x+1))
print("\n")

c=0
for x in m:
    if x < 0:
        c+=1
print(c)

print("\n")

d=0
for x in range(len(m)):
    if m[x] > d:
        d = m[x]

print(d)


print("\n")

# this is updated solution for returning the second largest number in an array. 
a = b = float('-inf')   
for x in m:
    if x > a:
        b = a
        a = x
    elif( x > b and x != a):
        b = x
print(b)





