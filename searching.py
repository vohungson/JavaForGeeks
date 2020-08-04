'''
Python code for searching algorithms
'''
import math

class search:
    def __init__(self, array, number):
        print("Array", array)
        print("Number: ", number)
        print("Linearly Search: ", self.linearlySearch(array, number))
        print("Binary Search: ", self.binarysearch(array, 0, len(array)-1, number))
        print("Jump Search: ", self.jumpSearch(array, number))
        print("InterPolation Search: ", self.interPolationSearch(array, number))
        print("Exponential Search: ", self.exponentialSearch(array, number))

    def exponentialSearch(self, array, number):
        if number < array[0] or number > array[len(array) - 1]: return -1
        if array[0] == number: return 0
        i = 1
        while i < len(array) and array[i] <= number: i *= 2
        return self.binarysearch(array, i/2, min(i, len(array)), number)

    def interPolationSearch(self, array, number):
        lo = 0
        hi = len(array) - 1
        while lo <= hi and array[lo] <= number and array[hi] >= number:
            if lo == hi:
                if array[lo] == number: return lo
                else: return -1
            pos = int(lo + (number - array[lo]) * (hi - lo) / (array[hi] - array[lo]))
            # change 'lo' and 'hi'
            if array[pos] == number: return pos
            elif array[pos] < number: lo = pos + 1
            else: hi = pos - 1
        return -1  # finish the function

    def jumpSearch(self, array, number):
        if array[0] > number or array[len(array) - 1] < number: return -1  # the number that we need to find is out of the range
        step = int (math.sqrt(len(array)))
        start = 0 # find the segment that the value is inside this segment
        while (start + step < len(array)): # find out "start" here
            if (array[start + step] < number): start += step
            else: break
        if start + step < len(array): end = start + step
        else: end = len(array) - 1
        while start <= end:
            if array[start] == number: break
            elif array[start] < number: start += 1
            else: return -1  # couldn't find out the position
        return start  # find out the position

    def binarysearch(self, array, l, r, number):
        if l <= r:
            mid = int((l + r) / 2)
            if array[mid] == number:
                return mid
            elif array[mid] < number: return self.binarysearch(array, mid + 1, r, number)
            else: return self.binarysearch(array, l, mid - 1, number)  # array[mid] > number
        else: return -1

    def linearlySearch(self, array, number):
        for i in range(len(array)):
            if array[i] == number: return i
        return -1

# Searching Main program
array = [0, 1, 1, 2, 3, 5, 8, 10, 21, 34, 55, 89, 144, 233, 377, 610]
number = 233
search(array, number)
