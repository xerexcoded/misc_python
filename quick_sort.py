def quick(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
        return quick(less) +[pivot]+ quick(greater)

print(quick([69,420,230000,1729]))

