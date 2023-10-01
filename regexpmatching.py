import time


class Solution:
    dict = {}

    def isMatch(self, s: str, p: str) -> bool:
        try:
            return self.dict[s + "_" + p]
        except:
            pass

        si = 0
        pi = 0

        while pi < len(p) and si <= len(s):
            # deal with *
            if pi + 1 < len(p) and p[pi+1] == "*":
                # repeat the letter before * and see if it matches
                for i in range(len(s[si:])+1):
                    # see if repeating part matches, if not we know we're done repeating so can assume false
                    if not self.isMatch(s[si: si+i], p[pi]*i):
                        self.dict[s + "_" + p] = False
                        return False
                    # elif pi + 2 ==len(s):
                    #     continue
                # see if the part after * matches, if not repeat loop with one more letter
                    elif self.isMatch(s[si+i:], p[pi+2:]):
                        self.dict[s + "_" + p] = True
                        return True
            elif si == len(s):
                self.dict[s + "_" + p] = False
                return False
            # Deal with .
            elif p[pi] == "." and len(s[si:]) > 0:
                si += 1
                pi += 1
                continue
            # deal with mismatches that are not . or *
            elif s[si] != p[pi]:
                self.dict[s + "_" + p] = False
                return False
            # Iterate the while loop and keep going
            si += 1
            pi += 1

        if si == len(s) and (pi == len(p) or len(p[pi:]) <= 2 and p[-1] == "*"):
            self.dict[s + "_" + p] = True
            return True
        self.dict[s + "_" + p] = False
        return False


start = time.time()
sol = Solution()
sol.isMatch("aa", "a")
fin = time.time()

print(fin - start)
