lass Solution(object):
    def isBalanced(self, num):
        oddsum=0
        evensum=0
        for i in range(len(num)):
            if i%2==0:
                evensum+=int(num[i])
            else:
                oddsum+=int(num[i])
        if evensum==oddsum:
            return True
        else:
            return False