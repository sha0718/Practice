def cartesian_product(sets):
    result = set()
    
    def backtrack(index, path):
        if index == len(sets):  # Base case: if we've selected from all sets
            result.add(tuple(path))  # Add the current path as a tuple to the result set
            return
        for num in sets[index]:  # Iterate through the current set
            path.append(num)  # Choose an element
            backtrack(index + 1, path)  # Recur to the next set
            path.pop()  # Backtrack to try the next element
    
    backtrack(0, [])
    return result
sets = [
    [1, 2],
    [3, 4],
    [5, 6, 7]
]

result = cartesian_product(sets)
for seq in result:
    print(seq)




            


 






    
 









