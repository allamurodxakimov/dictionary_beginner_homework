def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    c=0
    for i in data:
        if i["age"]==age:
            c+=1
            print(i)
    print("age = ",age)
    return c
print(count_users_with_age(data = [
  {
    'name': 'John',
    'age': 27
  },
  {
    'name':'Mary', 
    'age': 42
  },
  {
    'name':'Ann',
    'age': 27
  }
  ],age = 27))
print(count_users_with_age(data = [
  {
    'name': 'John', 
    'age': 35
  },
  {
    'name':'Mary', 
    'age': 20
  }
  ],age = 38))
