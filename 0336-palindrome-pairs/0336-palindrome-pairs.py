class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        result = []

        reverse_map = {}
        for i in range(len(words)):
            reversed_word = words[i][::-1]
            reverse_map[reversed_word] = i

        for i in range(len(words)):
            word = words[i]

            if "" in reverse_map and reverse_map[""] != i and word == word[::-1]:
                result.append([i, reverse_map[""]])
            
            for j in range(1, len(word) + 1):
                left = word[:j]
                right = word[j:]

                if right == right[::-1] and left in reverse_map and reverse_map[left] != i:
                    result.append([i, reverse_map[left]])

                if left == left[::-1] and right in reverse_map and reverse_map[right] != i:
                    result.append([reverse_map[right], i])

        return result
