def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less_than_pivot = []
    greater_than_pivot = []
    for item in arr[:-1]:
        if item < pivot:
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
array = [10,7,8,9,1,5]
sorted_array = quick_sort(array)
print("sorted array :",sorted_array)








            


 






    
 









