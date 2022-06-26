'''
    sort routines
'''


def mergeSort(sort_list):
    '''
        this is a merge sort routine
    '''
    my_list = sort_list
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # recursive call on each half
        left = mergeSort(left)
        right = mergeSort(right)

        item = 0
        count = 0
        loop = 0

        while item < len(left) and count < len(right):
            if left[item] <= right[count]:
                my_list[loop] = left[item]
                item += 1
            else:
                my_list[loop] = right[count]
                count += 1
            loop += 1
        while item < len(left):
            my_list[loop] = left[item]
            item += 1
            loop += 1

        while count < len(right):
            my_list[loop] = right[count]
            count += 1
            loop += 1
    return my_list


def bubbleSort(sort_list):
    '''
        bubblesort routine
    '''
    length = len(sort_list)
    for i in range(length - 1):
        for j in range(length-1-i):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
    return sort_list


def main():
    '''
        this is the main routine
    '''
    list1 = [100, 10, 3, 56, 4, 2, 65, 76, 23]
    list2 = [2, 3, 4, 10, 23, 56, 65, 76, 100]
    list3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    list4 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print("bubble sort     : ", list1, bubbleSort(list1) == list2)
    print("bubble sort     : ", list3, bubbleSort(list3) == list4)
    print("merge Sort      : ", list1, mergeSort(list1) == list2)
    print("merge Sort      : ", list3, mergeSort(list3) == list4)


if __name__ == '__main__':
    main()
