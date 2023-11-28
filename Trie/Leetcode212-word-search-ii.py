class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def create_trie(self, board):
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                temp = []
                for i, j in directions:
                    #print(f"(0 <= (r + i) < rows) and (0 <= (c + j) < cols) : {(0 <= (r + i) < rows) and (0 <= (c + j) < cols)}")
                    if (0 <= (r + i) < rows) and (0 <= (c + j) < cols):
                        #print(r+i,c+i)
                        temp.append(board[r + i][c + j])
                print(temp)
                curr = self.root
                for c in temp:
                    if c not in curr.children:
                        curr.children[c] = TrieNode()
                    #curr = curr.children[c]
                    curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        print(word)
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def findWords(self, board, words):
        res = []
        self.create_trie(board)
        for word in words:
            if self.search(word):
                res.append(word)
        return res


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
obj = Solution()
print(obj.findWords(board,words))