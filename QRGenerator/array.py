def fibonacci(n):
    fib_sequence = [0, 1]  # Start with the first two numbers

    # Generate the Fibonacci series until we reach n numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence[:n]  # Return the first n numbers

# Example usage
num_terms = 10  # Change this to generate more or fewer terms
print(fibonacci(num_terms))

      



            









    
 









