
n=5
# Pattern 1: Print nxn Star Square
# Print a square pattern of stars (*) of size n x n.

# Output
# * * * *
# * * * *
# * * * *
# * * * *
# Approach:
# ● Outer Loop (Rows): Run from i = 0 to i = n - 1
# ● Inner Loop (Columns): For each row, loop from j = 0 to j = n - 1
# ● Build Row String: Append *in each inner loop iteration.
# ● Print Row:After the inner loop, print the complete row string.
# Time & Space Complexity:
# Time Complexity:O(n^2)

# Space Complexity:O(n)(temporary row string)


for x in range(n):
    print(n*" * ")
    
print("\n")

for x in range(n):
    row = ""
    for y in range(n):
        row += " * "
    print(row)

# Output
# *
# * *
# * * *
# * * * *
# Approach:

for x in range(n+1):
    print(x*" * ")
    
print("\n")
for x in range(5):
    r=""
    for y in range(x+1):
        r+= " * "
    print(r)

print("\n")

# Output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# Approach:

for x in range(n):
    r=""
    for y in range(x+1):
        r = r + str(y+1)
    print(r)
    
for x in range(n):
    print("".join(str(y) for y in range(1, x+2)))

print("\n")

# 1
# 2 2
# 3 3 3
# 4 4 4 4
    
for x in range(n):
    r=""
    for y in range(x+1):
        r+= str(x+1)
    print(r)
    
# 1 2 3 4
# 1 2 3
# 1 2
# 1
    
for x in range(x,-1, -1):
    r=""
    for y in range(x):
        r+= str(y+1)
    print(r)


# 1
# 22
# 333
# 4444
# 55555


for x in range(5):
    for y in range(x+1):
        print(x+1, end = " ")
    print()



    
# 12345
# 1234
# 123
# 12
# 1

for x in range(5,-1,-1):
    r=""
    for y in range(x):
        r+= str(y+1)
    print(r)


for x in range(5):
    r=""
    for y in range(5-x):
        r+= str(y+1)
    print(r)

# *****
# ****
# ***
# **
# *

for x in range(5,-1,-1):
    for y in range(x):
        print("*", end = "")
    print()

#     *
#    **
#   ***
#  ****
# *****
for x in range(n):
    print(" "*(n-(x+1)), end="")
    for y in range(x+1):
        print("*", end="")
    print()


#     *
#    **
#   ***
#  ****
# *****

for x in range(5):
    r=""
    for y in range(5-(x+1)):
        r+=" "
    for z in range(x+1):
        r+="8 "
    print(r)



# 1
# 10
# 101
# 1010
# 10101

for x in range(5):
    r=""
    for y in range(x+1):
        if y % 2 == 0:
            r+=str(1)
        else:
            r+=str(0)
    print(r)

    
# 0
# 10
# 101
# 0101
# 01010

t=0
for x in range(5):
    r=""
    for y in range(x+1):
        r+=str(t)
        t=0 if t==1 else 1
    print(r)
