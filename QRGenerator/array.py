def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Step 3: Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are remaining elements in left or right, add them
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Example usage
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)







            


 






    
 









