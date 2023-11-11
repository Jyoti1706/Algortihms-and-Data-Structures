'''
time O(N)
space O(d)

Find Lowest common manager for a hierarchy
'''


# def getLowestCommonManager1(topManager, reportOne, reportTwo):
#     My Code failed for few cases
#     # Write your code here.
#     if reportOne in topManager.directReports or reportTwo in topManager.directReports:
#         return topManager
#     for node in topManager.directReports:
#         return getLowestCommonManager1(node, reportOne, reportTwo)

class OrgInfo:
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


def getOrgInfo(manager, reportOne, reportTwo):
    numofimportantReports = 0
    for dr in manager.directReports:
        orginfo = getOrgInfo(dr, reportOne, reportTwo)
        if orginfo.lowestCommonManager is not None:
            return orginfo
        numofimportantReports += orginfo.numImportantReports
    if manager == reportOne or manager == reportTwo:
        numofimportantReports += 1
    lowestCommonManager = manager if numofimportantReports == 2 else "None"
    return OrgInfo(lowestCommonManager, numofimportantReports)


def getLowestCommonManager(topManager, reportOne, reportTwo):
    # This is an input class. Do not edit.
    return getOrgInfo(topManager,reportOne,reportTwo).lowestCommonManager



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

print(getLowestCommonManager(A, E, I))