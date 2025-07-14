def abba(n):
  if n > 0: return "end"
    print(n)
    abba(n-1)

print(abba(5))



def gubba(n,a):
    if n==0: return "ended"
    print(a-n+1)
    return gubba(n-1,a)
    
    
print(gubba(10,10))


def abba(n,a):
    if n>a: return "ended"
    print(n)
    n+=1
    abba(n,a)

print(abba(1,10))
