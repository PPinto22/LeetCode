from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        word_len = len(words[0])
        word_dict = {word: words.count(word) for word in words}

        def isSubstring(i):
            temp_word_dict = {word: 0 for word in word_dict}
            for j in range(len(words)):
                word = s[i + j * word_len: i + j * word_len + word_len]
                if word in word_dict and word_dict[word] > temp_word_dict[word]:
                    temp_word_dict[word] += 1
                else:
                    return False
            else:
                return True

        return [i for i in range(len(s) - word_len * len(words) + 1)
                if isSubstring(i)]


def main():
    def readlines():
        for line in [
            "wordgoodgoodgoodbestword", ["word", "good", "best", "good"],
            "a", []
        ]:
            yield line

    lines = readlines()
    while True:
        try:
            s = next(lines)
            words = next(lines)

            ret = Solution().findSubstring(s, words)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
