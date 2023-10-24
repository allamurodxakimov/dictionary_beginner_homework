def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    s=0
    for i in data:
        if data.get(i)%2==0:
            s+=data.get(i)
    return "Sum even : ", s
print(sum_even_values(data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  }))
print(sum_even_values(data = {
    1: 22, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }))
    