def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    ls=[]
    for i in data:
        ls.append(i["age"])
        print(i)
    ls.sort()
    k=ls[0]
    for i in data:
        if i["age"]==k:
            print("Ism : ",i["name"])
print(get_min_age_user_name(data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]))
print(get_min_age_user_name(data = [
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