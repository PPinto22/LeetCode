from typing import List


class Trie:
    def __init__(self, letter):
        self.children = {}
        self.letter = letter
        self.end = False

    def add(self, word, i=0):
        letter = word[i]
        if letter not in self.children:
            self.children[letter] = Trie(letter)
        child = self.children[letter]
        if i == len(word) - 1:
            child.end = True
        else:
            child.add(word, i + 1)

    def has_prefix(self, word, i=-1):
        if i == len(word) - 1:
            return True
        letter = word[i] if i >= 0 else ''
        if letter != self.letter:
            return False

        next_letter = word[i + 1]
        return next_letter in self.children and self.children[next_letter].has_prefix(word, i + 1)

    def has_word(self, word, i=-1):
        if i == len(word) - 1:
            return self.end

        letter = word[i] if i >= 0 else ''
        if letter != self.letter:
            return False

        next_letter = word[i + 1]
        return next_letter in self.children and self.children[next_letter].has_word(word, i + 1)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0]) if board else 0

        trie = Trie('')
        for word in words:
            trie.add(word)

        solutions = set()

        def backtrack(cur, path, visited):
            i, j = cur
            if not trie.has_prefix(path):
                return
            if trie.has_word(path):
                solutions.add(''.join(path))

            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not (0 <= ni < n) or not (0 <= nj < m):
                    continue
                if (ni, nj) in visited:
                    continue
                path.append(board[ni][nj])
                visited.add((ni, nj))
                backtrack((ni, nj), path, visited)
                path.pop()
                visited.remove((ni, nj))

        for i in range(n):
            for j in range(m):
                backtrack((i, j), [board[i][j]], {(i, j)})
        return list(solutions)


if __name__ == '__main__':
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution().findWords(board, words))
