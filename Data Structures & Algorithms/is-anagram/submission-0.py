class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        ans = {}
        # Count characters in s
        for i in s:
            ans[i] = ans.get(i, 0) + 1
            
        # Subtract counts using characters in t
        for j in t:
            if j not in ans or ans[j] == 0:
                return False
            ans[j] -= 1
            
        return True