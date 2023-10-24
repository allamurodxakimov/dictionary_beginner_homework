def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    ls=[]
    for i in data:
        if (i["age"]) >= min_age and i["age"]<=max_age:
            ls.append((i["name"]))
    return ls
print(get_user_names_with_age_range(data = [
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
],min_age = 18,max_age = 25))
print(get_user_names_with_age_range(data = [
  {
    'name': 'Anny', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 30
  }
],min_age = 20,max_age = 30))