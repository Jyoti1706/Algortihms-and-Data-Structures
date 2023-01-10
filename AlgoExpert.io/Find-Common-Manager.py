# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

name=""
def lowestCommonManager(topManager, reportOne, reportTwo, count):
    global name
    if topManager.name == reportTwo or topManager.name == reportOne:
        return 1, topManager.name
    for children in topManager.directReports:
        if count == 2:
            return count,name
        loop=lowestCommonManager(children, reportOne, reportTwo, count)
        count = count+loop[0]
        name = loop[1]

    return count, topManager.name
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    count = 0
    return lowestCommonManager(topManager, reportOne, reportTwo, count)


A = OrgChart("A")
B = OrgChart("B")
C = OrgChart("C")
D = OrgChart("D")
E = OrgChart("E")
F = OrgChart("F")
G = OrgChart("G")
H = OrgChart("H")
I = OrgChart("I")

A.directReports = [B, C]
B.directReports = [D, E]
C.directReports = [F, G]
E.directReports = [H, I]
G.directReports = []
F.directReports = []
D.directReports = []

topManager = A
reportOne = "E"
reportTwo = "I"
print(getLowestCommonManager(topManager, reportOne, reportTwo))
