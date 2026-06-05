def linear_search(array, search_value):
    for index, element in enumerate(array):
        if element == search_value:
            return index
        elif element > search_value:
            break
        return None 
#Traverse every single cell, stop when required value found
#N steps taken at worst, O(n) complexity