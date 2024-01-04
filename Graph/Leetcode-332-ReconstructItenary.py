from collections import defaultdict
from typing import List


# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         city = defaultdict(list)
#         res = ["JFK"]
#         numOfTickets = len(tickets)
#         # generate math
#         for src, dest in tickets:
#             city[src].append(dest)
#
#         # Sorting of key for lexical order
#         for key in city:
#             city[key].sort()
#
#         def dfs(src, path):
#             path.append(src)
#             if len(path) == len(tickets) + 1:
#                 return True
#             neighbours = city[src][:]
#             for i, v in enumerate(neighbours):
#                 to_airport = city[src].pop(i)
#                 if dfs(to_airport, path):
#                     return True
#                 city[src].insert(i, to_airport)
#             path.pop()
#             return False
#
#         path = []
#         dfs("JFK", path)
#         if len(path) != len(tickets) + 1:
#             return []
#         # path.reverse()
#         return path

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Create graph of flights
        for start, end in sorted(tickets)[::-1]:
            graph[start].append(end)
        print(f"Graph: {graph}")
        route = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            route.append(node)

        dfs('JFK')
        print(f"route :: {route}")
        return route[::-1]


if __name__ == "__main__":
    obj = Solution()
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(obj.findItinerary(tickets))
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    # print(obj.findItinerary(tickets))
    # tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "JFK"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"], ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
    #            ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"]]
    print(obj.findItinerary(tickets))
