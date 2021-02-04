class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_word = False
        self.son = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """

        def insert_node(w):
            if len(w) == 0:
                node = Trie()
                node.is_word = True
                return node
            else:
                node = Trie()
                node.son[w[0]] = insert_node(w[1:])
                return node

        # 先进行前缀匹配
        loc = self
        i = 0
        while i < len(word) and word[i] in loc.son:
            loc = loc.son[word[i]]
            i += 1

        if i == len(word):
            loc.is_word = True
        else:
            loc.son[word[i]] = insert_node(word[i + 1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return self.is_word

        if word[0] in self.son:
            return self.son[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return True

        if prefix[0] in self.son:
            return self.son[prefix[0]].startsWith(prefix[1:])
        else:
            return False


t = Trie()
# t.insert('apple')
# print(t.search('apple'))
# print(t.search('app'))
# print(t.startsWith('app'))
t.insert('app')
t.insert('apple')
print(t.search('app'))
print(t.search('apple'))
