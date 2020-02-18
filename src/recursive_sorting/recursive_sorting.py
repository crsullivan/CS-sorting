# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO

    merged = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged.append(arrA[i])
            print(arrA[i])
            i += 1
        else:
            merged.append(arrB[j])
            j += 1
    merged = merged + arrA[i:] + arrB[j:]

    return merged

listA = [2,4,6,8]
listB = [1,3,5,7]
print(merge(listA, listB))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    arrayMid = len(arr) // 2
    arrA = arr[:arrayMid]
    arrB = arr[arrayMid:]

    print(arrayMid)
    print(arrA)
    print(arrB)

    mergedA = merge_sort(arrA)
    mergedB = merge_sort(arrB)
    
    print(mergedA)
    print(mergedB)

    done = merge(mergedA, mergedB)

    # i = 0
    # j = 0
    # k = 0

    # while i < len(arrA) and j < len(arrB):
    #     if arrA[i] < arrB[j]:
    #         merged[k] = arrA[i]
    #         i += 1
    #     else:
    #         merged[k] = arrB[j]
    #         j += 1
    #     k += 1

    # while i < len(arrA):
    #     merged[k] = arrA[i]
    #     i += 1
    #     k += 1

    # while j < len(arrB):
    #     merged[k] = arrB[j]
    #     j += 1
    #     k += 1

    return done


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
