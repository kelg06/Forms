def fixed_teen(a,b,c):
  if a < 9:
    pass
  elif a >= 10 and a < 15:
    a = 0
  elif a == 15 or a==16:
    pass
  elif a >= 17 and a <= 19:
    a = 0
  
  if b < 9:
    pass
  elif b >= 10 and b < 15:
    b = 0
  elif b == 15 or b==16:
    pass
  elif b >= 17 and b <= 19:
    b = 0
    
  if c < 9:
    pass
  elif c >= 10 and c < 15:
    c = 0
  elif c == 15 or c==16:
    pass
  elif c >= 17 and c <= 19:
    c = 0
  total=a+b+c
  return total
  




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