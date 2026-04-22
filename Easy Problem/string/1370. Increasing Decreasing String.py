class Solution(object):
    def sortString(self, s):

        sortS = "".join(sorted(s))
        result = []
        up = True   # increasing / decreasing control

        while sortS:

            # 🔼 Increasing order
            if up:
                last = ""
                temp = ""

                for ch in sortS:
                    if ch > last:
                        result.append(ch)
                        last = ch
                    else:
                        temp += ch

                sortS = temp

            # 🔽 Decreasing order
            else:
                last = "{"
                temp = ""

                for ch in reversed(sortS):
                    if ch < last:
                        result.append(ch)
                        last = ch
                    else:
                        temp = ch + temp

                sortS = temp

            up = not up   # direction change

        return "".join(result)