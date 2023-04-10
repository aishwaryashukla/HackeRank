
def is_unique(c,str):
    counter =0
    for i in range(len(s)):
        if c==s[i]:
            counter +=1
    if counter ==0 or counter >1:
        return False
    else:
        return True

s = 'abca'

for i in range(len(s)):
    if is_unique(s[i],s):
        print(s[i])
        break
