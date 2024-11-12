def fix(n):
  if n < 9:
    return n
  elif n >= 10 and n < 15:
    n = 0
    return n
  elif n == 15 or n == 16:
    return n
  elif n>= 17 and n <= 19:
    n = 0
    return n
  else:
    return n



def xyz_there(str):
  if str[0:3]== "xyz":
    return True
  for x in range(len(str)-3):
    if str [x] != "." and str[x + 1 : x + 4]=="xyz":
      return True
  return False


def centered_average(nums):
  nums.sort()
  total=0
  for i in range(1,len(nums)-1):
    total += nums[i]
  average = total/(len(nums)-2)
  return average