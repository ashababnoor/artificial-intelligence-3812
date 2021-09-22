import heapq

from numpy import e

graph = {0:'S', 1:'A', 2:'B', 3:'C', 4:'D'}

''' Tuple (x, y) indicates: to go to x node, the cost is y '''
adjc_list = [
    [(1, 1), (2, 4)],           # adjacency list for 0: 'S'
    [(2, 2), (3, 5), (4, 12)],  # adjacency list for 1: 'A'
    [(3, 2)],                   # adjacency list for 2: 'B'
    [(4, 3)],                   # adjacency list for 3: 'C'
    []                          # adjacency list for 4: 'D'
]

h_n = [7, 6, 2, 1, 0]           # heuristic values of nodes

class Node:
    total_cost_so_far = 0

    def __init__(self, node_no, prev, edge_cost, h_n):
        self.node_no = node_no
        self.prev = prev
        # self.g_n = Node.total_cost_so_far + edge_cost
        # self.f_n = self.g_n + h_n
        # Node.total_cost_so_far = self.g_n
        Node.total_cost_so_far += edge_cost
        self.f_n = Node.total_cost_so_far + h_n

    def __str__(self) -> str:
        return 'Node: ' + graph.get(self.node_no)

    def __repr__(self) -> str:
        return self.__str__() + ', Prev Node: ' + self.prev.__str__() + ', f_n = ' + str(self.f_n)

    def __lt__(self, other):
        return self.f_n < other.f_n


src_node = Node(0, None, 0, 0+h_n[0])
# print(src_node)
# print(src_node.__repr__())

heap = [src_node]
heapq.heapify(heap)

path = []

while len(heap) > 0:
    node_obj = heapq.heappop(heap)
    # print('Now popping:', node_obj.__repr__())
    path.append(node_obj)

    if node_obj.node_no == 4:
        break
    else:
        for adjc in adjc_list[node_obj.node_no]:
            edge_cost = adjc[1]
            node_no = adjc[0]
            new_node = Node(node_no, node_obj, edge_cost, h_n[node_no])
            heapq.heappush(heap, new_node)

            # print('Now adding:', new_node.__repr__())


for node in path:
    node_str = graph.get(node.node_no)
    print(node_str, end=' -> ')

print()
print('Total Cost:', Node.total_cost_so_far)

