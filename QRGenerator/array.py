def balanced_parens(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    result = []
    backtrack('', 0, 0)
    return result

# Example usage:
print(balanced_parens(0))  # Output: [""]
print(balanced_parens(1))  # Output: ["()"]
print(balanced_parens(2))  # Output: ["()()", "(())"]
print(balanced_parens(3))  # Output: ["()()()", "(())()", "()(())", "(()())", "(())()"]






            


 






    
 









