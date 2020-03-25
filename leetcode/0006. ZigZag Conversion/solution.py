class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = min(len(s), numRows)
        if rows <= 1:
            return s
        zygzag = []
        
        for j in range(rows):
            i = j
            zygzag.append(s[i])
            direction = 'down'
            while i < len(s):
                if direction == 'down':
                    delta = (rows - 1 - j) * 2
                    direction = 'up'
                elif direction == 'up':
                    delta = j * 2
                    direction = 'down'
                else:
                    raise ValueError
                
                i += delta
                if delta > 0 and i < len(s):
                    zygzag.append(s[i])
        return ''.join(zygzag)