class Node :

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node_2 = Node("B", None)
node_1 = Node("A", node_2)

print("nodo 2 data = ", node_2.data)
print("nodo 1 data = ", node_1.data)

#vemos sus siguientes
print("nodo 2 next = ", node_2.next)
print("nodo 1 next = ", node_1.next)
print("nodo 1 next = ", node_1.next.data)