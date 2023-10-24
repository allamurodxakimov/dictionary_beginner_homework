def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    ls=[]
    for i in data:
        ls.append(data.get(i))
    ls.sort()
    print(ls)
    return "max : ",ls[-1]
print(find_max_value(data = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3
  }))
print(find_max_value(data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }))