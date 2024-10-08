import functools
import inspect

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Initialize the call counter
        call_count = [0]

        # Helper function to count calls
        def count_inner_calls(inner_func, *inner_args, **inner_kwargs):
            # Increment call count
            call_count[0] += 1
            return inner_func(*inner_args, **inner_kwargs)

        # Modify the function to count calls
        original_function = func
        
        # Create a new function that counts calls to inner functions
        def counted_function(*inner_args, **inner_kwargs):
            return count_inner_calls(original_function, *inner_args, **inner_kwargs)

        # Replace the original function with the counted one temporarily
        globals()[func.__name__] = counted_function
        
        # Call the original function
        result = func(*args, **kwargs)

        # Restore the original function
        globals()[func.__name__] = original_function

        return call_count[0], result

    return wrapper

# Example usage
@count_calls
def example_function(x):
    if x > 0:
        return example_function(x - 1) + x
    return 0

# Call the function and print results
calls, result = example_function(5)
print(f"Number of calls: {calls}, Result: {result}")









            


 






    
 









