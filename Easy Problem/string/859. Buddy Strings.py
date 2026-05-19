class Solution(object):
    def buddyStrings(self, s, goal):

        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]