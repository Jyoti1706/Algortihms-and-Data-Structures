def getLowestCommonManager1(topManager, reportOne, reportTwo):
    # Write your code here.
    if reportOne in topManager.directReports or reportTwo in topManager.directReports:
        return topManager
    for node in topManager.directReports:
        return getLowestCommonManager(node, reportOne, reportTwo)


def getLowestCommonManager(top):
    # This is an input class. Do not edit.
    pass


class OrgInfo:
    def __int__(self, lowestcommonmanager, numImportantReports):
        self.lowestCommonManager = lowestcommonmanager
        self.numImportantReports = numImportantReports


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


A = OrgChart("A")
B = OrgChart("B")
C = OrgChart("C")
D = OrgChart("D")
E = OrgChart("E")
F = OrgChart("F")
G = OrgChart("G")
H = OrgChart("H")
I = OrgChart("I")

A.directReports = [B,C]
B.directReports = [D,E]
C.directReports = [F,G]
D.directReports = [H,I]

print(getLowestCommonManager(A, E, I).name)