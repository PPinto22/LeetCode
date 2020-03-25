class Solution:
    def __init__(self):
        self.mem = {}
    
    def isMatch(self, s: str, p: str, i=0, j=0) -> bool:
        if j >= len(p):
            return i >= len(s)
        
        current_match = i < len(s) and p[j] in [s[i], '.']
        
        if (i,j) in self.mem:
            result = self.mem[(i,j)]
        else:
            if j+1 < len(p) and p[j+1] == '*':
                result = (current_match and self.isMatch(s, p, i+1, j)) or self.isMatch(s, p, i, j+2)
            else:
                result = current_match and self.isMatch(s, p, i+1, j+1)
            self.mem[(i,j)] = result
            
        return result