def factorial(n):
    if n < 0:
        return None  # Return None for negative inputs
    elif n == 0 or n == 1:
        return "1"  # Base case: 0! and 1! are both 1
    
    result = "1"  # Initialize result as a string
    for i in range(2, n + 1):
        result = multiply_strings(result, str(i))
    
    return result

def multiply_strings(num1, num2):
    # Initialize the result as a list of zeros
    result = [0] * (len(num1) + len(num2))
    
    # Reverse both numbers to multiply from least significant digit
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            # Multiply and add to the appropriate position in result
            result[i + j] += digit1 * digit2
            # Handle carry over
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
            
    # Remove leading zeros and convert to string
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return ''.join(map(str, result[::-1]))  # Reverse back and convert to string

# Example usage
print(factorial(5))   # Output: "120"
print(factorial(25))  # Output: "15511210043330985984000000"
print(factorial(-1))  # Output: None










            


 






    
 









