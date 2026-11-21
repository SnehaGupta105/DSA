class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        last_seen = {}
        new_children = [[] for _ in range(n)]
        def dfs(node):
            ch = s[node]
            old = last_seen.get(ch, -1)
            if old != -1:
                new_parent = old
            else:
                new_parent = parent[node]
            if node != 0:
                new_children[new_parent].append(node)
            last_seen[ch] = node
            for child in children[node]:
                dfs(child)
            if old == -1:
                del last_seen[ch]
            else:
                last_seen[ch] = old
        dfs(0)
        answer = [1] * n
        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]
        calculate(0)
        return answer