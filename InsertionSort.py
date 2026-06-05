def insertion_sort(array):
    for index in range(1, len(array)): #each pass
        temp_value = array[index] #creates temp val. 
        position = index - 1

        while position >=0:
            if array[position] > temp_value: #is value here greater
                array[position + 1] = array[position] #shift into gap
                position = position -1 #shift to next left value
            else:
                break
        array[position+1] = temp_value
    return array

#O(n^2) complexity, N^2 + 2N - 2 steps.