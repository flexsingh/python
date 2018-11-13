def bubbleSort(list):
  print("original list:", list)
  length = len(list)
  for i in range(length -1):
    for j in range(length-1-i):
      if (list[j] > list[j+1]):
        list[j], list[j+1] = list[j+1], list[j]
  print("sorted list:", list)

list1 = [100,10,3,56,4,2,65,76,23]
bubbleSort(list1)
