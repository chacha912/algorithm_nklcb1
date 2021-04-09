class TrieNode:
    def __init__(self, value=None):
        self.value = value 
        self.count = {}
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        length = len(word)
        for idx, char in enumerate(word):
            left_length = length - idx
            if char not in node.children:
                node.children[char] = TrieNode(char)
            if left_length not in node.count:
                node.count[left_length] = 1
            else:
                node.count[left_length] += 1  
            node = node.children[char]
        node.children['*'] = TrieNode()

    def search(self, query):
        node = self.root
        length = len(query)
        for idx, char in enumerate(query):
            if char == '?':
                cnt = length - idx
                if cnt in node.count:
                    return node.count[cnt]
                else:
                    return 0
            if char not in node.children:
                return 0
            node = node.children[char]
        
def solution(words, queries):
    trie = Trie()
    reverse_trie = Trie()
    answer = []

    for word in words:
        trie.insert(word)
        reverse_trie.insert(word[::-1])

    for query in queries:
        if query[0] == '?':
            answer.append(reverse_trie.search(query[::-1]))
        else:
            answer.append(trie.search(query))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries)) # [3, 2, 4, 1, 0]