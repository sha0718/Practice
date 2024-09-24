def binary_search(sorted_list,target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = low + high // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
sorted_toys = [1,3,8,9,10,23]
print(binary_search(sorted_toys ,23))







            


 






    
 









