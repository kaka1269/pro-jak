def get_first_index(numbers):
    first_index = False
    index = None 
    for i in range(len(numbers)):
        if numbers[i] == 7 and first_index == False:
            index = i
            first_index = True
    return index
numbers=[
    [1,4,5,2,4,7,7,2,7],
    [1,4,7,2,4,7,7,2,7],
    [1,7,5,2,4,7,7,2,7],
    [7,4,5,2,4,7,7,2,7],
]
for i in range(len(numbers)):
    print(get_first_index(numbers[i]))
        
    