"""
Jose-Antonio Rubio
CS 325-400
HW 1
MergeSort
Sources:
    read in user input: https://www.pythonforbeginners.com/system/python-sys-argv
    measure run time:  https://docs.python.org/2/library/timeit.html
"""
import sys
import timeit
from random import randint

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


def runMergeSort(data):  
    n = len(data) 
    start = timeit.default_timer()
    mergeSort(data)
    runtime = timeit.default_timer() - start
    print("n = "+ str(n))
    print("time: "+str(runtime))
           



def generateArray(n):
	arr = []
	for i in range(0, n):
		arr.append(randint(0, 10000))
	runMergeSort(arr)


count = sys.argv[1]
generateArray(int(count))