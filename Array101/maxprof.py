p = [7,6,4,3,1]
mini, prof = p[0],0
for i in range(1, len(p)):
    if p[i] - mini > prof:
        prof = p[i] - mini
    
    if p[i] < mini:
        mini = p[i]
        
print(prof)
