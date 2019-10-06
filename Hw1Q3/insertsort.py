"""
Jose-Antonio Rubio
CS 325-400
HW 1
MergeSort
"""

# Insert sort will look at each element in the array
# and compare it to the previous elements  that are 
# already checked and thus already sorted
def insertSort(arr):
   for j in range(1,len(arr)):
     key = arr[j]
     i = j
     while i>0 and arr[i-1]>key:
         arr[i]=arr[i-1]
         i = i-1
     arr[i]=key


def runInsertSort():
    # write to an output file
    output = open("insert.txt", 'w+') 
    with open("data.txt", 'r') as file:
        for line in file:
            data=[int(num) for num in line.split()]
            # pop the first element as that is the size of the array and not to be sorted
            n = data.pop(0)
            insertSort(data)
            output.write(' '.join(str(x) for x in data)+"\n")
    output.close()


runInsertSort()
