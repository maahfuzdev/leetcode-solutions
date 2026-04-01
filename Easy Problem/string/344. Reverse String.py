def reverseString( s):
        new_List=[]
        for i in range(len(s)-1,-1,-1):
            new_List.append(s[i])
        return new_List
print(reverseString(["h","e","l","l","o"]))      