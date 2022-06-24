'''
    bubblesort routine
'''


def bubbleSort(sort_list):
    '''
        bubblesort routine
    '''
    length = len(sort_list)
    for i in range(length - 1):
        for j in range(length-1-i):
            if (sort_list[j] > sort_list[j+1]):
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
    return sort_list


def main():
    '''
        this is the main routine
    '''
    list1 = [100, 10, 3, 56, 4, 2, 65, 76, 23]
    list2 = [2, 3, 4, 10, 23, 56, 65, 76, 100]
    print(list1, bubbleSort(list1) == list2)


if __name__ == '__main__':
    main()
