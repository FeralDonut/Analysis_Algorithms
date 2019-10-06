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


def runInsertSort(data):
    n = len(data) 
    start = timeit.default_timer()
    insertSort(data)
    runtime = timeit.default_timer() - start
    print("n = "+ str(n))
    print("time: "+str(runtime))
           



def generateArray(n):
	arr = []
	for i in range(0, n):
		arr.append(randint(0, 10000))
	runInsertSort(arr)


count = sys.argv[1]
generateArray(int(count))