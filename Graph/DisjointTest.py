class DisjointSet:
    def __init__(self, n):
        self.rank = [0 for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.parent = [i for i in range(n + 1)]

    def findUpar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUpar(self.parent[node])
        return self.parent[node]

    def unionbyRank(self, u, v):
        ulp_u = self.findUpar(u)
        ulp_v = self.findUpar(v)
        if ulp_v == ulp_u:
            return
        if self.rank[ulp_v] > self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionbySize(self, u, v):
        ulp_u = self.findUpar(u)
        ulp_v = self.findUpar(v)
        if ulp_v == ulp_u:
            return
        if self.size[ulp_v] < self.size[ulp_u]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]


if __name__ == "__main__":
    disDS = DisjointSet(7)
    disDS.unionbySize(1, 2)
    disDS.unionbySize(2, 3)
    disDS.unionbySize(4, 5)
    disDS.unionbySize(6, 7)
    disDS.unionbySize(5, 6)

    if disDS.findUpar(3) == disDS.findUpar(7):
        print("Same Parent")
    else:
        print("Not same")

    disDS.unionbySize(3, 7)
    if disDS.findUpar(3) == disDS.findUpar(7):
        print("Same Parent")
    else:
        print("Not same")
