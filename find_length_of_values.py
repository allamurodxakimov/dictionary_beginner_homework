def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    c=0
    for i in data:
        c+=len(data.get(i))
        k=len(data.get(i))
        print(data.get(i),"lenght = ",k)
    return c
print(find_length_of_values( data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }))