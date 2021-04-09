### Trie 문제 해결

#### 프로그래머스 가사 검색 문제

[프로그래머스 가사 검색 문제링크](https://programmers.co.kr/learn/courses/30/lessons/60060)

```python
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

```

### 💡

- 검색할 단어를 Trie로 저장한다.
- Trie 만들 때 count 속성을 추가하여 {n:m} 정보도 저장한다. (해당 노드 뒤에 n 자리수의 단어가 m 개 있음)
- 쿼리문에 ? 가 맨뒤에 있을 경우, ? 를 만나면 node.count에서 ? 의 개수인 n에 해당하는 단어수 m을 출력한다.
- 쿼리문 맨 앞에 ?가 있을 경우에는 전부 순회하며 검색해야 하므로, 단어를 거꾸로 저장한 Trie를 만들고 쿼리문도 거꾸로 검색을 하면 위의 방법을 사용할 수 있다.

- `Trie 만들 때 필요한 정보를 저장하는 속성 추가하기 `
- `? 이 앞에있을 경우, 뒤에있을 경우를 다른 방법으로 해결할 수도 있지만, 같은 방법으로 적용할 수 있는지도 생각해보기`
