def merge_sort(arr):
    def merge(list1, list2):
      posin1 = 0
      while True:
        try:
          if posin1 == 0 and list2[0] < list1[0]:
            list1.insert(0, list2[0])
            del list2[0]
          if len(list2) == 0:
            return list1
          if list1[posin1] <= list2[0] <= list1[posin1+1]:
            list1.insert(posin1+1, list2[0])
            posin1 += 1
            del list2[0]
          else:
            posin1 += 1
          if posin1 > len(list1)-1:
            break
        except IndexError:
          list1.extend(list2)
          return list1
      list1.extend(list2)
      return list1
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]
    return merge(merge_sort(left), merge_sort(right))
