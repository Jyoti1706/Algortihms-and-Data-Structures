def sunsetview(building, direction):

    building_count = len(building)
    East=[0]*building_count
    West=[0]*building_count
    j = building_count-1
    while j >= 0:
        #print(building[j])
        if j==building_count-1:
            East[j] = 0
        else:
            East[j]=max(East[j+1],building[j+1])
        j = j-1
    j=0
    while j < building_count:
        if j==0:
            West[j]=0
        else:
            West[j] = max(West[j-1], building[j-1])
        j=j+1
    output = []
    if direction == 'East':
        i = 0
        while i < building_count:
            if East[i] < building[i]:
                output.append(i)
            i=i+1
    else:
        i = 0
        while i < building_count:
            if West[i] < building[i]:
                output.append(i)
            i=i+1
    return output
building = [3, 5, 4, 4, 3, 1, 3, 2]
print(sunsetview(building,'East'))
print(sunsetview(building,'West'))