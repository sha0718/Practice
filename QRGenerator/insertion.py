def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i -1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor   
if __name__ =='__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3,9,7,11],
        [25,22,21,10],        
        [29,15,28],
        [], 
        [7]       
    ]
    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array : {elements}')