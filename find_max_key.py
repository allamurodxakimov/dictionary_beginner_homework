def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    ls=[]
    for i in data:
        ls.append(i)
    ls.sort()
    print(data)
    return "key max : ",ls[-1]
print(find_max_key(data = {
    1: 'a', 
    2: 'b', 
    3: 'c'
  }))
print(find_max_key(data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }))