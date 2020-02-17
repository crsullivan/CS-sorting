# TO-DO: Complete the selection_sort() function below 
# arr = [2,3,0,4,7,8,9,1]
# print(arr)

def selection_sort( set ):
    # loop through n-1 elements
    for i in range(0, len(set) - 1):
        cur_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(set)):
            if set[cur_index] > set[j]:
                cur_index = j
        # TO-DO: swap
        set[i], set[cur_index] = set[cur_index], set[i]
    return set

print(selection_sort([7,3,8,1,9,6]))

# print(selection_sort(arr))
# print(arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr

print(bubble_sort([7,3,8,1,9,6]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr