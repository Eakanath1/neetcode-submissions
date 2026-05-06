"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        new_nodes = dict()
        new_nodes[node] = Node(node.val)
        q = deque([node])
        while q:
            original = q.popleft()
            for neighbor in original.neighbors:
                if neighbor not in new_nodes:
                    new_nodes[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                new_nodes[original].neighbors.append(new_nodes[neighbor])
        return new_nodes[node]