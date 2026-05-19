class Solution(object):
    def strongPasswordCheckerII(self, password):

        x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        y = "abcdefghijklmnopqrstuvwxyz"
        z = "!@#$%^&*()-+"
        d = "1234567890"

        c1 = c2 = c3 = c4 = 0

        # length check
        if len(password) < 8:
            return False

        # consecutive character check
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False

        # character category check
        for j in password:
            if j in x:
                c1 += 1
            elif j in y:
                c2 += 1
            elif j in z:
                c3 += 1
            elif j in d:
                c4 += 1
            else:
                return False

        # final condition
        if c1 >= 1 and c2 >= 1 and c3 >= 1 and c4 >= 1:
            return True
        else:
            return False