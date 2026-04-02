def reverseStr(s, k):
        l=[]
        h=[]
        i=0
        while i<len(s):
            l.append(s[i:i+k])
            i=i+k
        for j in range(len(l)):
            if j%2==0:
                h.append(l[j][::-1])
            else:
                h.append(l[j])
        return ''.join(h)   
print(reverseStr("abcdefg",2))            