class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longestStr = ''
        currentStr = ''
        currentSet = set()
        i = 0

        while i < len(s):
            char_ = s[i]
            if char_ not in currentSet:
                currentStr += char_
                currentSet.add(char_)
            else:
                if len(currentStr) > len(longestStr):
                    longestStr = currentStr

                # Restart search from the first occurence of char_ in currentString
                char_i = currentStr.find(char_)
                i = i - len(currentStr) + char_i + 1
                currentStr = s[i]
                currentSet = {s[i]}
            i += 1
        if len(currentStr) > len(longestStr):
            longestStr = currentStr
        return len(longestStr)


def stringToString(input):
    import json

    return json.loads(input)


def main():
    lines = [
        "dvdf"
    ].__iter__()
    while True:
        try:
            s = next(lines)
            # s = stringToString(line);

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()