'''
Python code for sorting
'''

class Sorting:
    def __init__(self,array):
        print("Python code for sorting")
        print("Original Array: ", array)
        print("Selection Sort: ", self.selectionSort(array))
        print("Bubble Sort: ", self.bubbleSort(array))

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

array = [64, 25, 12, 22, 11]
Sorting(array)