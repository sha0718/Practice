import heapq

def nth_hamming_number(n):
    # A min-heap to store the Hamming numbers
    hamming_numbers = []
    # A set to keep track of unique Hamming numbers
    seen = set()
    
    # Start with the first Hamming number
    heapq.heappush(hamming_numbers, 1)
    seen.add(1)
    
    # The variable to hold the nth Hamming number
    hamming_number = 1
    
    for _ in range(n):
        # Get the smallest Hamming number from the heap
        hamming_number = heapq.heappop(hamming_numbers)
        
        # Generate the next Hamming numbers
        for factor in [2, 3, 5]:
            new_hamming_number = hamming_number * factor
            if new_hamming_number not in seen:
                seen.add(new_hamming_number)
                heapq.heappush(hamming_numbers, new_hamming_number)
    
    return hamming_number

# Example usage:
print(nth_hamming_number(1))   # Output: 1
print(nth_hamming_number(2))   # Output: 2
print(nth_hamming_number(3))   # Output: 3
print(nth_hamming_number(4))   # Output: 4
print(nth_hamming_number(5))   # Output: 5
print(nth_hamming_number(20))  # Output: 35
print(nth_hamming_number(100)) # Example of a higher number








            


 






    
 









