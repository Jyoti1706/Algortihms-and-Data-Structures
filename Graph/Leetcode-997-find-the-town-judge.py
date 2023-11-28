from collections import defaultdict
class Solution:
    def create_adjacencyList(self, edge_list):
        adj_lst = defaultdict(set)
        for edge in edge_list:
            node1, node2 = edge
            adj_lst[node1].add(node2)
        return adj_lst

    def findJudgeBruteForce(self, n: int, trust):
        trust_list = self.create_adjacencyList(trust)
        key = trust_list.keys()
        if n == 1 and trust == []:
            return n
        if len(key) == n - 1:
            val_set = dict()
            for key, val in trust_list.items():
                for v in val:
                    val_set[v] = val_set.get(v, 0) + 1
            for key in val_set:
                if val_set[key] == n - 1:
                    return key
            return -1
        else:
            return -1

    def findJudge(self, n: int, trust):
        """
        1. keep trust on list
        2. keep trust by list
        iterate and increase trust[i][0] node count by 1 for truston(out degree) list index
        and increase count for trust by also
        at the end check for any array element whose trust by (indegree) count is n-1 and trust on is Zero
        :param n:
        :param trust:
        :return:
        """





trust = [[1,3],[2,3],[3,1]]
#trust = [[1,3],[2,3]]
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
trust = [[1,3],[2,3]]
#trust = []
obj = Solution()
print(obj.findJudge(2,trust))
