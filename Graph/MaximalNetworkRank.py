from collections import defaultdict


def create_adjacency_list(edge_list):
    adjacency_list = defaultdict(set)

    for edge in edge_list:
        node1, node2 = edge

        # Adding node2 to the adjacency list of node1
        adjacency_list[node1].add(node2)

        # Adding node1 to the adjacency list of node2 (assuming the graph is undirected)
        adjacency_list[node2].add(node1)

    return adjacency_list
class Solution:
    def maximalNetworkRank1(self, n: int, roads):
        adjlst = create_adjacency_list(roads)
        max_rank = -1
        for edge in roads:
            max_rank = max(len(adjlst[edge[0]]) + len(adjlst[edge[1]]) - 1, max_rank)
        return max_rank

    def maximalNetworkRank(self, n: int, roads):
        adjlst = create_adjacency_list(roads)
        roads = set([tuple(road) for road in roads])
        # print(roads)
        max_rank = 0
        adjlst_node = list(adjlst.keys())
        n = len(adjlst_node)
        for i in range(n):
            l1 = len(adjlst[adjlst_node[i]])
            for j in range(i + 1, n):
                l2 = len(adjlst[adjlst_node[j]])
                if (adjlst_node[i], adjlst_node[j]) in roads or (adjlst_node[j], adjlst_node[i]) in roads:
                    rank = l1 + l2 - 1
                else:
                    rank = l1 + l2
                max_rank = max(max_rank, rank)
        return max_rank


n = 5
roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]

n = 6
roads = [[2, 4]]
obj = Solution()
print(obj.maximalNetworkRank(n, roads))
