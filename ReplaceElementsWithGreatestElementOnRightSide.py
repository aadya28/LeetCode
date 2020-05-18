def replaceElements(arr):
    maximum = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        temp = arr[i]
        arr[i] = maximum
        if(temp>maximum):
            maximum = temp

    return arr



listIn = [17,18,5,4,6,1]
print(replaceElements(listIn))

