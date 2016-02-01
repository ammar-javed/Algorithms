def bubble_sort( array ):
    ''' array -> int array
        Sorting by doing adjacent comparisons repeatedly 
        through the array, until everything is sorted '''

    to_be_sorted = len( array ) - 1

    while to_be_sorted > 0:

        for i in range( to_be_sorted ):
            if array[i] > array [i+1]:
                array[i], array[i+1] = array[i+1], array[i]

        to_be_sorted -= 1

    return array

if __name__ == "__main__":
    example_one = []
    print "Test: "
    print example_one
    print "Output: "
    print bubble_sort( example_one )

    example_two = [12342, 12341] 
    print "Test: "
    print example_two
    print "Output: "
    print bubble_sort( example_two )

    example_three = [1232, 123, 21, 341, 231, 32135, 123, 3, 2, 5, 231, 993, 7, 3, 4, 4, 4]
    print "Test: "
    print example_three
    print "Output: "
    print bubble_sort( example_three )
