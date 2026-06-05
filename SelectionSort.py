def selection_sort(array):
    for i in range(len(array) - 1): #pass through
        lowest_number_index = i #track lowest value index, increment every pass

        for j in range(i+1, len(array)): #checks if there's a lower value than current
            if array[j] < array[lowest_number_index]:
                lowest_number_index = j #yes, thats the new idx
        
        if lowest_number_index!=i: #not the starting val anymore?
            #swap
            array[i], array[lowest_number_index] = array[lowest_number_index], array[i]
    return array

#Starts from first idx, moves and tracks idx of lowest value. 
#Swaps lowest and the one it started at. Moves to new idx in new passthrugh.

#O(n^2) complexity, but faster than bubblesort by n^2/2 steps (half the steps)
