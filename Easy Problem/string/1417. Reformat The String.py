class Solution(object):
    def reformat(self, s):
       sortS=s
       digit = ""
       letter = ""
       result=""

       for ch in s:
         if ch.isdigit():
          digit += ch
         elif ch.isalpha():
          letter += ch
       if abs(len(digit) - len(letter))>1:
        return result
       else:
        if len(digit)==len(letter):
          for i in range(len(digit)):
             result+=digit[i]+letter[i]
          return result
        elif len(digit)>len(letter):
             for i in range(len(letter)):
                result+=digit[i]+letter[i]
             result=result + digit[len(digit)-1]
             return result
        else:
            
               for i in range(len(digit)):
                 result+=letter[i]+digit[i]
               result=result + letter[len(letter)-1]  
               return result      
                
       
               

        