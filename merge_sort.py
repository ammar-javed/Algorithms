def merge_sort( array ):
    ''' array -> int array
        Recursively call merge_sort with subarrays of the original,
        until all sub arrays are sorted and can be merges using the sort
        criteria. '''

    # If the size of the array is 0 or 1, 
    # then it is already sorted
    if len(array) < 2:
        return array

    # calculate the middle of the array (round down)
    mid = len(array) // 2

    # Sort the subarrays
    left_sub_array = merge_sort(array[0:mid])
    right_sub_array = merge_sort(array[mid:])

    # Init variables
    sorted_array = []
    left_index = 0
    right_index = 0

    # xrange to utilize a generator instead of generating the entire range in memory
    for i in xrange(len(array)):

        # If we have gone through one sub array, then just append the rest of
        # the other sub array
        if left_index == len(left_sub_array):
            sorted_array += right_sub_array[right_index:]
            break
        elif right_index == len(right_sub_array):
            sorted_array += left_sub_array[left_index:]
            break

        # Otherwise append the smaller of the two numbers the indices are currently on.
        if left_sub_array[left_index] < right_sub_array[right_index]:
            sorted_array.append(left_sub_array[left_index])
            left_index += 1
        else:
            sorted_array.append(right_sub_array[right_index])
            right_index += 1

    return sorted_array

if __name__ == "__main__":
    example_one = []
    print "Test: " 
    print example_one
    print "Output: "
    print merge_sort(example_one)

    example_two = [12342]
    print "Test: " 
    print example_two
    print "Output: "
    print merge_sort(example_two)

    example_three = [1232, 123, 21, 341, 231, 32135, 123, 3, 2, 5, 231, 993, 7, 3, 4, 4, 4]
    print "Test: "
    print example_three
    print "Output: "
    print merge_sort(example_three)
