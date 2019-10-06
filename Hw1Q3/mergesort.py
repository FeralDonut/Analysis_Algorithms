"""
Jose-Antonio Rubio
CS 325-400
HW 1
MergeSort
"""

# Merge will merge the two arrays together in ascending order
def merge(arr, p, q, r):
    i=0
    j=0
    k=0
    while i < len(p) and j < len(r):
        if p[i] < r[j]:
            arr[k]=p[i]
            i=i+1
        else:
            arr[k]=r[j]
            j=j+1
        k=k+1
    while i < len(p):
        arr[k]=p[i]
        i=i+1
        k=k+1
    while j < len(r):
        arr[k]=r[j]
        j=j+1
        k=k+1

# Merge sort wil recursively call itself to divide 
# the array down to smaller elements to be sorted
def mergeSort(arr):
    if len(arr)>1:
        q = len(arr)//2
        p = arr[:q]
        r = arr[q:]
        mergeSort(p)
        mergeSort(r)
        merge(arr, p, q, r)


def runMergeSort():
    # write to an output file
    output = open("merge.txt", 'w+') 
    with open("data.txt", 'r') as file:
        for line in file:
            data=[int(num) for num in line.split()]
            # pop the first element as that is the size of the array and not to be sorted
            n = data.pop(0) 
            mergeSort(data)
            output.write(' '.join(str(x) for x in data)+"\n")
    output.close()

runMergeSort()