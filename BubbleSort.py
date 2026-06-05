def bubble_sort(array):
    unsorted_until_index = len(array) - 1
    #tracks the rightmost index not yet sorted, initialised as final idx
    sorted = False #tracks if sorted or not. Initially its not

    while not sorted:
        sorted = True #åssume sorted till we encounter a swap
        #if we get through the entire array with none it becomes true
        #and loop breaks
        for i in range(unsorted_until_index):
            if array[i] > array[i+1]:
                array[i], array [i+1] = array[i+1], array[i] #swap
                sorted = False #swap made hence false
        unsorted_until_index -=1

    return array

#Swap two consecutive, move on till end reached. Largest pushed to end
#Another pass through, repeat till no swaps in a passthrough

#O(n^2) complexity