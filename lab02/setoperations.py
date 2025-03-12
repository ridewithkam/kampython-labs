# sets time

def make_set(data):
    if data is None:
        return []
    
    new_list = []
    for num in data:
        if num not in new_list:
            new_list.append(num)

    return new_list

def is_set(data):
    if data is None:
        return False # none isnt a set
    
    seen = []
    for num in data:
        if num in seen:
            return False
        seen.append(num) # if not, add number to list

def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    
    new_list = []
    for num in setA:
        new_list.append(num)
    
    for num in setB:
        if num not in new_list:
            new_list.append(num)
    
    return new_list
    
def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []

    new_list = []
    for num in setA:
        if num in setB:
            new_list.append(num)
    
    return new_list

print(make_set([1, 2, 3, 4, 5]))
print(is_set([1, 2, 3, 4, 5]))
print(is_set([5, 5]))
print(union([1, 2], [2, 3]))
print(intersection([1,2], [2, 3]))