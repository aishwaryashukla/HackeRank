def distance_from_zero(number):
  if (isinstance(number, int)) or isinstance(number, float):
    return abs(number)
  else:
    return "Nope"


print(distance_from_zero(True))
print(isinstance(True, int))
