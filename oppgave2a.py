
liste = [0,1,2,3,4,5,6,7,8,9,10]
#sorted_to_balanced(liste)


def sorted(sorted_arr, start, end):
    if start > end:
        return
    
    middle = (start + end) // 2
    print(sorted_arr[middle])

    sorted(sorted_arr, start, middle -1)
    sorted(sorted_arr, middle + 1, end)

sorted(liste, 0, len(liste)-1)