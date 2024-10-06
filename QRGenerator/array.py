def is_circularly_sorted(arr):
    if not arr:  # Handle empty array
        return True
    
    n = len(arr)
    break_count = 0
    
    for i in range(n):
        # Compare current element with the next element
        if arr[i] > arr[(i + 1) % n]:
            break_count += 1
            
        # If we have more than one break, it's not circularly sorted
        if break_count > 1:
            return False
            
    return True

# Example usage:
print(is_circularly_sorted([2, 3, 4, 5, 0, 1]))       # Output: True
print(is_circularly_sorted([4, 5, 6, 9, 1]))          # Output: True
print(is_circularly_sorted([10, 11, 6, 7, 9]))        # Output: True
print(is_circularly_sorted([1, 2, 3, 4, 5]))          # Output: True
print(is_circularly_sorted([5, 7, 43, 987, -9, 0]))   # Output: True
print(is_circularly_sorted([1, 2, 3, 4, 1]))          # Output: True

print(is_circularly_sorted([4, 1, 2, 5]))              # Output: False
print(is_circularly_sorted([8, 7, 6, 5, 4, 3]))       # Output: False
print(is_circularly_sorted([6, 7, 4, 8]))              # Output: False
print(is_circularly_sorted([7, 6, 5, 4, 3, 2, 1]))    # Output: False







            


 






    
 









