from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def hash_(row):
            code = 0
            for i, cell in enumerate(reversed(cells)):
                code += cell*(10**i)
            return code

        def simulate(row):
            new_row = [0] * len(row)
            for i, cell in enumerate(row):
                if i == 0 or i == len(row) - 1:
                    new_row[i] = 0
                elif row[i-1] == row[i+1]:
                    new_row[i] = 1
                else:
                    new_row[i] = 0
            return new_row

        days = [cells.copy()]
        seen = {hash_(cells): 0}
        for i in range(1, N+1):
            cells = simulate(cells)
            days.append(cells.copy())
            code = hash_(cells)
            if code not in seen:
                seen[code] = i
                continue

            loop_start = seen[code]
            loop_len = i - loop_start
            return days[loop_start + ((N - loop_start) % loop_len)]

        return cells


if __name__ == '__main__':
    print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7000002))