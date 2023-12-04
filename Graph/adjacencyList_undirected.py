from collections import defaultdict


def create_GraphList(edge_list):
    adjacency_list = {}

    for edge in edge_list:
        node1, node2 = edge

        # Adding node2 to the adjacency list of node1
        if node1 in adjacency_list:
            adjacency_list[node1].append(node2)
        else:
            adjacency_list[node1] = [node2]

        # Adding node1 to the adjacency list of node2 (assuming the graph is undirected)
        if node2 in adjacency_list:
            adjacency_list[node2].append(node1)
        else:
            adjacency_list[node2] = [node1]

    return adjacency_list


def create_GraphSet(edge_list):
    adjacency_list = defaultdict(set)

    for edge in edge_list:
        node1, node2 = edge

        # Adding node2 to the adjacency list of node1
        adjacency_list[node1].add(node2)

        # Adding node1 to the adjacency list of node2 (assuming the graph is undirected)
        adjacency_list[node2].add(node1)

    return adjacency_list
# Example usage:
# edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# adj_list = create_adjacency_list_2(edges)
#
# # Display the result
# for node, neighbors in adj_list.items():
#     print(f"{node}: {neighbors}")