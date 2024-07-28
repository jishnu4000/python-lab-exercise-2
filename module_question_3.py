# Question 3
# (a)
def merging_Dict(*args: dict) -> dict:
  """
    Takes multiple dictionaries and merges them into one.
    
    Args:
    *dicts: Arbitrary number of dictionaries
    
    Returns:
    dict: The final merged dictionary
  """
  result = dict()
  for arg in args:
    # unpacking operators: * (for tuples) and ** (for dictionaries)
    # result = {**result, **arg} 
    # merge | operator
    result = result | arg
  return result

# (b)
def common_Keys(*args: dict) -> set:
  """
    Finds common keys across multiple dictionaries.
    
    Args:
    *dicts: Arbitrary number of dictionaries
    
    Returns:
    set: The set with all common keys
  """
  # if no input return empty dictionary
  if not args:
    return {}
  
  # start with keys of first dict
  result = set(args[0].keys())
  
  for arg in args[1:]:
    # find common keys and update to remove other keys
    result.intersection_update(arg.keys())
  
  return result

# (c)
def invert_Dict(arg: dict) -> dict:
  """
    Inverts a dictionary, swapping keys and values.
    If multiple keys have the same value, groups these keys in a list in the inverted dictionary.
    
    Args:
    dict: Dictionary to be inverted
    
    Returns:
    dict: The dictionary with inverted key-value pairs
  """
  result = {}
  for key, val in arg.items():
    if val in result:
      if isinstance(result[val], list):
        result[val].append(key)
      else:
        result[val] = [result[val], key]
    else:
      result[val] = key
  return result

# (d)
def common_Pairs(*args: dict) -> dict:
  """
    Finds common key-value pairs across multiple dictionaries.
    
    Args:
    *dicts: Arbitrary number of dictionaries
    
    Returns:
    dict: A dictionary containing the common key-value pairs
    """
  # if no input return empty dictionary
  if not args:
    return {}
  
  # start with first dict items as a set
  result = args[0].items()

  for arg in args[1:]:
    # find common pairs and update result set
    # & operator performs intersection between sets
    result = result & (arg.items())
  
  return dict(result)
