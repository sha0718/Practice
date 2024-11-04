def linear_search(my_list,target):
    for index, item in enumerate(my_list):
        if item == target:
            return index
    return -1
toys = ['car','doll','ball']
print(linear_search(toys,'doll'))            