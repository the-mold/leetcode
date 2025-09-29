class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        _length = len(arr) - 1
        zeroes_to_duplicate = 0

        # 1. first count all zeros that you can double
        for i in range(_length):
            if i + zeroes_to_duplicate > _length:
                break

            if arr[i] == 0:
                # edge casE: if get 0 but only one place left in the array, you cannot double the 0.
                # put the zero as last element and decrease the _length in preparation of step 2.
                if i + zeroes_to_duplicate == _length:
                    arr[_length] = 0
                    _length -= 1
                    break

                zeroes_to_duplicate += 1
        
        # 2. Go from back to front in order not to miss numbers(see screenshot)
        last_actual_element = _length - zeroes_to_duplicate
        for i in range(last_actual_element, -1, -1):
            if arr[i] == 0:
                arr[i+zeroes_to_duplicate] = 0
                zeroes_to_duplicate -= 1
                arr[i+zeroes_to_duplicate] = 0
            else:
                arr[i+zeroes_to_duplicate] = arr[i]

#T:O(n)
#S:O(1)