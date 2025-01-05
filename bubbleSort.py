import random as r
import time as t
input = []

for i in range(1000):
    input.append(r.randint(1, 1001))

def bubbleSort(input):
    lastIdx = len(input) - 1
    while lastIdx > 0:
        swap = False
        for i in range(lastIdx):
            if input[i] > input[i + 1]:
                swap = True
                tmp = input[i + 1]
                input[i + 1] = input[i]
                input[i] = tmp
        if not swap:
            return input
        lastIdx = lastIdx - 1
    return input

def selectionSort(input):
    for i in range(len(input)):
        minIdx = findMin(input, i)
        if minIdx != i:
            tmp = input[i]
            input[i] = input[minIdx]
            input[minIdx] = tmp
    return input

def findMin(input, startIdx):
    minIdx = startIdx
    for i in range(startIdx + 1, len(input)):
        if input[minIdx] > input[i]:
            minIdx = i
    return minIdx

def insertionSort(input):
    result = [None] * len(input)
    result[0] = input[0]
    lastInsertedIdx = 0
    for iIdx in range(1, len(input)):
        #rIdx = lastInsertedIdx + 1
        #while rIdx != 0:
        #    rIdx = rIdx - 1
        for rIdx in reversed(range(lastInsertedIdx + 1)):
            if input[iIdx] > result[rIdx]:
                lastInsertedIdx = lastInsertedIdx + 1
                result[rIdx + 1] = input[iIdx]
                break
            else:
                result[rIdx + 1] = result[rIdx]
                if rIdx == 0:
                    result[rIdx] = input[iIdx]
                    lastInsertedIdx = lastInsertedIdx + 1
    return result

def mergeSort(input):

    return result

def merge(arr1, arr2):
    result = []
    arr1Idx = 0
    arr2Idx = 0
    while arr1Idx < len(arr1) or arr2Idx < len(arr2):
        if arr1[arr1Idx] < arr2[arr2Idx]:
            result.append(arr1[arr1Idx])
            arr1Idx = arr1Idx + 1
        else:
            result.append(arr2[arr2Idx])
            arr2Idx = arr2Idx + 1
    if arr1Idx == len(arr1):
        copyRemainder(result, arr2Idx, arr2)
    else:
        copyRemainder(result, arr1Idx, arr1)
    return result

def copyRemainder(result, idx, arr):
    while idx < len(arr):
        result.append(arr[idx])
        idx = idx + 1


def withMeasure(func):
    cpInput = list(input)
    start_time = t.time()
    sorted  = func(cpInput)
    print("%s --- %s seconds ---" % (func.__name__, t.time() - start_time))
    return sorted

print(withMeasure(insertionSort))
print(withMeasure(selectionSort))
print(withMeasure(bubbleSort))
