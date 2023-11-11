def generatedivtaghelper(prefix, open, close, results):
    if open>0:
        newprefix = prefix+"<div>"
        generatedivtaghelper(newprefix,open-1,close, results)
    if close>open:
        newprefix = prefix + "</div>"
        generatedivtaghelper(newprefix, open,close-1, results)
    if close == 0:
        results.append(prefix)


def generateDivTags(numberOfTags):
    # Write your code here.
    results = []
    generatedivtaghelper("",numberOfTags,numberOfTags,results)
    return results

print(generateDivTags(3))