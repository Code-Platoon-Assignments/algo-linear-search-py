def linear_search(value_to_find, array_to_search_through):

    idx = 0
    for item in array_to_search_through:
        if item == value_to_find:
            return idx
        idx+=1
    
    return None

def linear_search_global(value_to_find, array_to_search_through):
    
    idx = 0
    returnArr = []
    for item in array_to_search_through:
        if item == value_to_find:
            returnArr.append(idx)
        idx+=1

    if len(returnArr)>0:
        return returnArr
    
    return None