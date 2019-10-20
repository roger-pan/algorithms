def quick_sort(lst, l_index, r_index, pivot):

    def _qsort_helper(l_index, r_index , pivot):
        l_index = l_index
        r_index = r_index
        pivot = pivot

    _qsort_helper(lst[0],lst[len(lst)-1],round(len(lst)/2))

    def swap(a, b):
        lst[b], lst[a] = lst[a], lst[b]

    swap_left = False
    swap_right = False
    p = pivot
    pivot_value = lst[pivot]

    # While loop runs as long as both l_index and right_index aren't at the pivot, i.e. the sort has not finished
    while (l_index < pivot or r_index > pivot):
        # Setting the conditions for a swap to take place
        if swap_left and swap_right:
            swap(l_index, r_index)
            swap_left = False
            swap_right = False
            l_index += 1
            r_index -= 1
        # If index on the left is smaller than the pivot value, move onto the next index
        if lst[l_index] < pivot_value:
            l_index += 1
        else:
            swap_left = True
        # If index on the right is bigger than the pivot value, move onto the next index
        if lst[r_index] > pivot_value:
            r_index -= 1
        # Else move onto the next index
        else:
            swap_right = True
        # if left index is at the pivot and right index is not done
        if l_index == pivot:
        # If right side needs to be swapped
            if swap_right:
                pivot = r_index
                l_index +=1
            else:
                r_index -=1
        if r_index == pivot:
            if swap_left:
                pivot = l_index
                r_index -=1
            else:
                l_index = 1


l = [2,3,55,10,59,45,36,59]
quick_sort(l,0,7,4)
print(l)







