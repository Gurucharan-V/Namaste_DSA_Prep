# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]



# O(n+x) thiem complixity but it same thing ultimetly its a same thing!
x = 0
for i in range(len(p)):
  if p[i] != 0:
    p[x] = p[i]
    x+=1

for i in range(x, len(p)):
  p[x] = 0

# here O(n)
for i in range(len(p)):
  if p[i] != 0 and p[x] ==0:
    p[i],p[x]=p[x],p[i]

  if p[x] != 0:
    x+=1


  
