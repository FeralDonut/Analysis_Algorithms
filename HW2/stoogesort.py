"""
Jose-Antonio Rubio
CS 325-400
HW 2
Stooge Sort
"""

import sys
import timeit
from random import randint

def stoogeSort(arr, i, j):
    # Base Case
    if i >= j: 
        return
   
    
    if arr[i]>arr[j]: 
        temp = arr[i] 
        arr[i] = arr[j] 
        arr[j] = temp
   
    # Check to see if there are more than two elements
    # in the array
    if j-i + 1 > 2: 
        n = (int)((j-i + 1)/3) 
   
        # Rucrusively call on the 
        # first 2/3 then the next 2/3
        # and again on the first 2/3
        stoogeSort(arr, i, (j-n)) 
        stoogeSort(arr, i + n, (j)) 
        stoogeSort(arr, i, (j-n))
           

def runStoogeSort(data):
    n = len(data) 
    start = timeit.default_timer()
    stoogeSort(data, 0, n-1)
    runtime = timeit.default_timer() - start
    print("n = "+ str(n))
    print("time: "+str(runtime))

def generateArray(n):
	arr = []
	for i in range(0, n):
		arr.append(randint(0, 10000))
	runStoogeSort(arr)


count = sys.argv[1]
generateArray(int(count))