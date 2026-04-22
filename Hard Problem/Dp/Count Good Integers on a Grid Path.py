class Solution:
    def countGoodIntegersOnPath(self, l, r, dirs):

        a = [0] * 16
        r1 = 0
        c1 = 0
        a[0] = 1

        for c in dirs:
            if c == "D":
                r1 += 1
            else:
                c1 += 1
            a[(r1 << 2) | c1] = 1

        def calc(s):

            dp_cache = [[[-1] * 10 for _ in range(16)] for _ in range(2)]

            def dp(pos, is_less, last):
                if pos == 16:
                    return 1

                if is_less and dp_cache[1][pos][last] != -1:
                    return dp_cache[1][pos][last]

                limit = 9 if is_less else int(s[pos])

                ans = 0

                for i in range(limit + 1):

                    if a[pos] and i < last:
                        continue

                    nxt_last = i if a[pos] else last
                    nxt_less = is_less or (i < limit)

                    ans += dp(pos + 1, nxt_less, nxt_last)

                if is_less:
                    dp_cache[1][pos][last] = ans

                return ans

            return dp(0, False, 0)

        sL = str(l - 1).zfill(16)
        sR = str(r).zfill(16)

        return calc(sR) - calc(sL)