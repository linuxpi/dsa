class Node:
    
    def __init__(self, value, children = None, isEnd = False):
        self.value = value
        self.children = children or {}
        self.isEnd = isEnd
    

    def add_child(self, c):
        if c not in self.children:
            self.children[c] = Node(c)
        
        return self.children[c]
    
    def has_child(self, c):
	return self.children.get(c)
    
class Trie:
    
    def __init__(self):
        self.root = Node("")
    
    def insert(self, word):
        if not word:
            return
        node = self.root
        for c in word:
            node = node.add_child(c)
        
        node.isEnd = True
    
    def search(self, word):
        node = self.root
        word_len = len(word)
        for index, c in enumerate(word):
            node = node.has_child(c)
            if not node:
                break

	    print node.value, node.children, node.isEnd, index, word_len
            if node.isEnd and index == word_len - 1:
                return True
            
        return False
            
    
def construct_trie(words):
    trie = Trie()

    for word in words:
        trie.insert(word)    
        
    return trie
		

def search_word(word, trie):
	max_length = len(word)
	for index in range(max_length + 1):
		sub_word = word[0:index]

		is_present = trie.search(sub_word)

		if is_present:
			print index, max_length
			if index == max_length or search_word(word[index:max_length], trie):
				return True

    	return False

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        trie = construct_trie(wordDict)
        return search_word(s, trie)
        
        


print Solution().wordBreak("leetcode", ["leet","code"])
print Solution().wordBreak("leetcod", ["leet","code"])
print Solution().wordBreak("lecode", ["le", "leet","code"])
print Solution().wordBreak("leetcode", ["le", "leet","code"])
print Solution().wordBreak("leetcode", ["le","code"])

print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
