"""
Jose-Antonio Rubio
CS 325-400
HW 4
Last-to-Start
Comment:    Reusing MergeSort from HW1
"""

# Merge will merge the two arrays together in ascending order by finish time
def merge(arr, p, q, r):
    i=0
    j=0
    k=0
    while i < len(p) and j < len(r):
        if p[i][2] < r[j][2]:
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

def lastToStart(array):
    mergeSort(array)
    n = len(array)
    arr = []
    i = n - 1
    arr.append(array[i][0])
    # compare the current finish time of j to the start time of previous start time i 
    for k, j in reversed(list(enumerate(array))):  
       if j[2] <= array[i][1]:
            arr.append(j[0])
            i = k
    return list(reversed(arr))

with open('act.txt') as inFile:
    array = []
    set_number = 1
    # parse through file and make an array of arrays for each set
    for line in inFile:
        line = line.rstrip()
        if len(array) and ' ' not in line :
            if(len(array[0]) > 1):
                activities = lastToStart(array[0:])
            else:
                activities = lastToStart(array[1:])
            print("Set: " + str(set_number))
            print("Number of activities selected = " + str(len(activities)))
            print("Activities: " + str(activities)[1:-1])
            set_number += 1
            array = []
            print('\n')
        else:
            array.append([int(i) for i in line.split()])

    # print the last set to the terminal
    if len(array) > 0:
        activities = lastToStart(array)
        print("Set: " + str(set_number))
        print("Number of activities selected = " + str(len(activities)))
        print("Activities: " + str(activities)[1:-1])