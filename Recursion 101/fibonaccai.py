def feb(n):
    if n ==0 or n ==1: return n
    elif n>1: return feb(n-1)+feb(n-2)
print(feb(12),"\n")

a,b = 0,1
for i in range(6):
    a,b = b,a+b
    
print(a,"\n")


a,b,n = 0,1,6
for i in range(n+1):
    print(a)
    a,b = b,a+b
