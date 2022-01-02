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
                time.sleep(max_time - (speedInput() * max_time / 100))

        i += 1

    colorArray = ['green'] * N
    displayArray(arr, colorArray, swapCount)
    print("Sorted arr : ",arr)



# arr = [2, 10,11,25,13,78,1,7,80]
# print(bubbleSort(arr))
