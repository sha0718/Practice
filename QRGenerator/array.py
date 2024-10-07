def dbl_linear(n):
    u = [1]  # Start the sequence with the first element
    i, j = 0, 0  # Two pointers for generating the sequence

    while len(u) <= n:  # Generate until we reach the nth element
        next_x = 2 * u[i] + 1
        next_y = 3 * u[j] + 1
        
        # Choose the smaller value to maintain order
        if next_x < next_y:
            u.append(next_x)
            i += 1
        elif next_x > next_y:
            u.append(next_y)
            j += 1
        else:  # They are equal, we can only add one of them
            u.append(next_x)
            i += 1
            j += 1

    return u[n]

# Example usage:
print(dbl_linear(10))  # Output should be 22
print(dbl_linear(20))
print(dbl_linear(30))
print(dbl_linear(50))





            


 






    
 









