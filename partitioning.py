class SortableArray:
    def __init__(self, array):
        self.array = array

    def partition(self, left_pointer, right_pointer):
        pivot_index - right_pointer
        pivot = self.array[pivot_index]
        right_pointer -= 1

        while True:
            while self.array[left_pointer] < pivot:
                left_pointer += 1
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                left_pointer += 1
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]

        return left_pointer
