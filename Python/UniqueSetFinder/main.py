numbers=[1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1]

def remove_duplicates(input_list):
    return list(set(input_list))
print(remove_duplicates(numbers))