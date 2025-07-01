def countfuntion(n):
    if n == 0:
        return 1
    elif n == -:
        return "minus doesnt print here sheeeeh"
    n=abs(n)
    counter = 0 
    for x in range(len(str(n))):
        n=n//10
        counter +=1
    return counter

print(countfuntion(-))


def countfuntion(n):
    if n == 0:
        return 1
    n=abs(n)
    counter = 0 
    # for x in range(len(str(n))):
    while(n>0):
        n=n//10
        counter +=1
    return counter

print(countfuntion(123123123))
