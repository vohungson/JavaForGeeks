'''
Python code for sorting
'''

class Sorting:
    def __init__(self):
        array = [64, 25, 12, 22, 11]
        print("Python code for sorting")
        print("0. Original Array: ", array)
        print("1. Selection Sort: ", self.selectionSort(array))
        array = [64, 25, 12, 22, 11]
        print("2. Bubble Sort: ", self.bubbleSort(array))
        array = [64, 25, 12, 22, 11]
        print("3. Insertion Sort: ", self.insertionSort(array))
        array = [64, 25, 12, 22, 11]
        print("4. Merge Sort: ", self.mergeSort(array))
        array = [64, 25, 12, 22, 11]
        self.quickSort(array, 0, len(array)-1)
        print("5. Quick Sort: ", array)

    def quickSort(self, array, low, high):
        if low < high:
            pivot = self.partition(array, low, high)
            self.quickSort(array, low, pivot - 1)
            self.quickSort(array, pivot + 1, high)

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    def mergeSort(self, array):
        if len(array) > 1:
            mid = len(array)//2
            arrayLeft = array[:mid]
            arrayRight = array[mid:]
            self.mergeSort(arrayLeft)
            self.mergeSort(arrayRight)

            i = j = k = 0
            while i < len(arrayLeft) and j < len(arrayRight): # copy data from two sub array to the array
                if arrayLeft[i] < arrayRight[j]:
                    array[k] = arrayLeft[i]
                    i += 1
                else:
                    array[k] = arrayRight[j]
                    j += 1
                k += 1

            while i < len(arrayLeft):  # copy the remaining numbers in the arrayLeft to the array
                array[k] = arrayLeft[i]
                i += 1
                k += 1

            while j < len(arrayRight):  # copy the remaining numbers in the arrayRight to the array
                array[k] = arrayRight[j]
                j += 1
                k += 1
        return array

    def insertionSort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        return array

    def bubbleSort(self, array):
        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if array[i] > array[j]: array[i], array[j] = array[j], array[i]
        return array

    def selectionSort(self, array):
        for i in range(len(array)-1):
            minIndex = i
            for j in range(i+1, len(array)):
                if array[minIndex] > array[j]: minIndex = j
            array[i], array[minIndex] = array[minIndex], array[i]
        return array


Sorting()