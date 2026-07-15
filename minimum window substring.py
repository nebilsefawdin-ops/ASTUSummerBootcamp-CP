class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = 0
        missing = len(t)
        ans = ""

        for right in range(len(s)):
            if s[right] in need:
                if need[s[right]] > 0:
                    missing -= 1
                need[s[right]] -= 1

            while missing == 0:
                if ans == "" or right - left + 1 < len(ans):
                    ans = s[left:right+1]

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        missing += 1
                left += 1

        return ans
        
