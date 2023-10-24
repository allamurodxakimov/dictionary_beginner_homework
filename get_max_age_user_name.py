def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    print(data)
    ls=[]
    for i in data:
        print(i)
        ls.append(i["age"])
    ls.sort()
    k=ls[-1]
    for i in data:
        if i["age"]==k:
            print(i["name"])
    return k
print(get_max_age_user_name(data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]))
print(get_max_age_user_name(data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
]))