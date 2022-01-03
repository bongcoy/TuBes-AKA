import time

max_time = 0.250

def bubbleSort(arr, displayArray, speedInput, pauseBool):

    N = len(arr)
    swapped = True
    i = 0
    swapCount = 0

    while i < N and swapped:
        swapped = False

        for j in range(N - 1):

            if arr[j] > arr[j + 1]:
                #swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                swapCount += 1

                colorArray = ['red'] * N
                colorArray[j] = 'blue'
                colorArray[j + 1] = 'blue'
                
                if i:
                    colorArray[-i:] = ['green'] * i

                displayArray(arr, colorArray, swapCount)
                print("Sorting arr : ",arr)
                time.sleep(max_time - (speedInput() * max_time / 100))

        i += 1

    colorArray = ['green'] * N
    displayArray(arr, colorArray, swapCount)
    print("Bubble Sorted arr : ",arr)
