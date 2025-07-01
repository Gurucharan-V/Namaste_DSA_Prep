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
