def abba(n):
  if n > 0: return "end"
    print(n)
    abba(n-1)

print(abba(5))



def gubba(n,a):
    if a==n: return "ended"
    print(a-n+1)
    abba(n+1,a)
    
    
print(abba(1,10))
