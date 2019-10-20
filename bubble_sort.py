
def bubble_sort(lst):
    """
    Sorts a list from smallest to largest using the bubble sort algorithm
    """

    def swap(i,j):
        lst[i], lst[j] = lst[j], lst[i]

    n = 0
    while n <= len(lst) - 1:
        for i in range(len(lst)-1-n):
            if lst[i] >= lst[i+1]:
                    swap(i,i+1)
        n+=1

