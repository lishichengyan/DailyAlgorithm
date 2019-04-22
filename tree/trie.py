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
