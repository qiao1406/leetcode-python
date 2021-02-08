class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if len(wordList) == 0 or endWord not in wordList:
            return 0

        if beginWord in wordList:
            wordList.remove(beginWord)

        word_set = set(wordList)
        step = 1
        bs = {beginWord}
        es = {endWord}
        letters = [chr(97 + i) for i in range(26)]
        visited = set()

        while bs and es:
            if len(es) < len(bs):
                es, bs = bs, es

            next_layer = set()

            for word in bs:
                for i in range(len(word)):
                    for letter in letters:
                        new_word = word[:i] + letter + word[i + 1:]

                        if new_word == word:
                            continue
                        if new_word in word_set:
                            if new_word in es:
                                return step + 1
                            if new_word not in visited:
                                next_layer.add(new_word)
                                visited.add(new_word)

            step += 1
            bs = next_layer

        return 0


s = Solution()
print(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
print(s.ladderLength("lost", "cost", ["most", "fist", "lost", "cost", "fish"]))
print(s.ladderLength("set",
                     "oar",
                     ["oar", "sat", "dip", "sir", "lap", "tat", "off", "din", "caw", "hob", "lie", "tam", "wyo", "noe",
                      "rob", "nay", "hah", "box", "mac", "low", "tin", "tip", "set", "geo", "too", "tea", "fin", "tad",
                      "zed", "key", "ray", "shy", "min", "kin", "rep", "now", "ink", "fag", "fed", "pas", "huh", "bad",
                      "oks", "pan", "kip", "inc", "bat", "pop", "pat", "aol", "cud", "tan", "car", "hut", "oat", "gap",
                      "hes", "hen", "chi"]))
