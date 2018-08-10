'''
14.1 Clone Graph
描述
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbour
OJ’s undirected graph serialization: Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbour
node. As an example, consider the serialized graph {0,1,2#1,2#2,2}.
The graph has a total of three nodes, and therefore contains three parts as separated by #.
1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
2. Second node is labeled as 1. Connect node 1 to node 2.
3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:
1
/ \
/ \
0 --- 2
/ \
\_/
'''
#
# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @BFS0
    def cloneGraph(self, node):
        def dfs(input, map):
            if input in map:
                return map[input]
            output = UndirectedGraphNode(input.label)
            map[input] = output
            for neighbor in input.neighbors:
                output.neighbors.append(dfs(neighbor, map))
            return output
        if node == None: return None
        return dfs(node, {})


node1=UndirectedGraphNode(1)
node0=UndirectedGraphNode(0)
node2=UndirectedGraphNode(2)
node1.neighbors=[node0,node2]
node0.neighbors=[node1,node2]
node2.neighbors=[node1,node0,node2]
mySolu=Solution()
NewNode=mySolu.cloneGraph(node1)
print(NewNode.label)



