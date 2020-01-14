# LeetCode 208
class TrieNode:
    def __init__(self):
        self._isEnd = False;
        self._children = [None] * 26
        
    def get(self, ch: str) -> object:
        return self._children[ord(ch) - ord('a')]
    
    def put(self, ch: str, node: object) -> None:
        self._children[ord(ch) - ord('a')] = node
        
    def isEnd(self) -> bool:
        return self._isEnd
    
    def setEnd(self) -> None:
        self._isEnd = True
    
    def containsKey(self, ch: str) -> bool:
        return self._children[ord(ch) - ord('a')] != None
    
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
#####################################################################################################
class TrieNode:
    def __init__(self):
        self.ch = None  # 储存字符
        self.cnt = 0  # 标记从这个节点到根节点字符串出现了几次
        self.is_end = False  # 标记是不是完整的单词
        self.children = [None]*26  # 子节点
    
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        tmp = self.root
        for ch in s:
            key = ord(ch) - ord('a')
            if tmp.children[key] is None:
                tmp.children[key] = TrieNode()
                tmp.children[key].ch = ch
                tmp.children[key].cnt += 1
                if ch == s[-1]:
                    tmp.children[key].is_end = True
            else:
                tmp.children[key].cnt += 1
                if ch == s[-1]:
                    tmp.children[key].is_end = True
            tmp = tmp.children[key]
            
    def has(self, s):
        tmp = self.root
        for ch in s:
            key = ord(ch) - ord('a')
            if tmp.children[key] is None:
                return False
            elif tmp.children[key].ch == ch:
                tmp = tmp.children[key]
        return True
    
    def delete(self, s):
        # 只有当s是一个完整的单词才删除
        # 待续。。。
    
    # 好像有点点问题...
    def get_occurance(self, s):
        tmp = self.root
        for ch in s:
            key = ord(ch) - ord('a')
            if tmp.children[key] is None:
                return 0
            elif tmp.children[key].ch == ch:
                tmp = tmp.children[key]
        return tmp.cnt
                

t = Trie()
t.insert("abcd")
t.insert("abe")
t.insert("afg")
t.insert("ah")
t.insert("ah")
t.insert("ah")

print(t.get_occurance("ah"))

####################################
# leetcode 1032
class TrieNode:
    def __init__(self):
        self.ch = None  # unecessary for this problem
        self.is_end = False
        self.children = [None]*26
        
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        tmp = self.root
        n  = len(s)
        for i in range(n):
            ch = s[len(s) - 1 - i]
            key = ord(ch) - ord('a')
            if tmp.children[key] is None:
                tmp.children[key] = TrieNode()
                tmp.children[key].ch = ch
            else:
                tmp.children[key].ch = ch
            tmp = tmp.children[key]
        tmp.is_end = True
        
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.s = ""
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        self.s = letter + self.s
        tmp = self.trie.root
        for ch in self.s:
            key = ord(ch) - ord('a')
            if tmp.children[key] is None:
                return False
            elif tmp.children[key].is_end is True:
                return True
            else:
                tmp = tmp.children[key]
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
