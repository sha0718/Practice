def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i] ,arr[min_index] = arr[min_index],arr[i]


if __name__ == '__main__':
    tests = [
        [14,65,78,45,35,23,90],
        [13,15,18,16,34,21],
        [],
        [29,72,64,62],
        [7,5,23]
    ]
    for elements in tests:
      selection_sort(elements)  
      print(elements)