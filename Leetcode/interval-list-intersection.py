l1=[[0,2],[5,10],[13,23],[24,25]]
l2 = [[1,5],[8,12],[15,24],[25,26]]

def intervalIntersection(l1,l2):
    len_l1 = len(l1)
    len_l2= len(l2)
    i=0
    j=0
    output = []
    while i<len_l1 and j<len_l2:
        csp = max(l1[i][0], l2[j][0])
        cep = min(l1[i][1], l2[j][1])
        if csp > cep:
            if l1[i][0] < l2[j][0]:
                i = i+1
            else:
                j=j+1
        elif csp < cep:
            output.append([csp,cep])
            if l1[i][1] < l2[j][1]:
                i=i+1
            else:
                j=j+1
        else:
            output.append([csp,cep])
            if l1[i][1] < l2[j][1]:
                i=i+1
            else:
                j=j+1

    return output

print(intervalIntersection(l1,l2))


