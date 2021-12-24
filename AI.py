class Node:
    
    def __init__(self):
        self.val = ''
        self.left = None
        self.right = None

class Solution:
    
    def getName(self):
        s = input("Enter your name ")
        return s
    
    def main(self):
        root = self.getTree()
        name = self.getName()
        self.putPreorder(root, name)
        self.getPreorder(root)
        
    def getTree(self):
        root = Node()
        q = [root]
        k = 31
        while k > 0:
            nxt = []
            for cur in q:
                l, r = Node(), Node()
                cur.left = l
                cur.right = r
                nxt.extend([l, r])
                k -= 2
            q = nxt
        return root
    
    def putPreorder(self, root, name):
        self.pos = 0
        N = len(name)
        
        def dfs(cur):
            if self.pos == N: return
            if not cur: return
            if cur.left == cur.right == None:
                cur.val = name[self.pos]
                self.pos += 1
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)
        
    def getPreorder(self, root):
        
        def dfs(cur):
            if not cur: return
            print(cur.val, end='')
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)
        
sol = Solution()
sol.main()
