
class Node:
    def __init__(self, value):
        self._value = value
        self._child = []
    
    def __repr__(self):
        return 'Node %s'%str(self._value)

    def add_child(self, node):
        self._child.append(node)
    
    def __iter__(self):
        return iter(self._child)

    def dfs(self):
        yield self
        for n in self._child:
            for x in n.dfs(): yield x
    
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child1.add_child(Node(5))
    for n in root.dfs():
        print n
