from django.shortcuts import render
from app.forms import *
from app.fix_teen import *
# Create your views here.
def front_times(request):
  form = FrontTimes(request.GET)
  if form.is_valid():
    n = form.cleaned_data['number']
    string = form.cleaned_data['string']
    

    front_len = 3
    if front_len > len(string):
        front_len = len(string)
    front = string[:front_len]
    result = ""
    for i in range(n):
        result = result + front
    return render(request, "front.html", {"form": form, "result": result})
    
  return render(request, "front.html", {"form": form})

def fix_teen(request):
  form = FixTeen(request.GET)
  if form.is_valid():
    a= form.cleaned_data['a']
    b= form.cleaned_data['b']
    c= form.cleaned_data['c']

    num_a = fix(a)
    num_b = fix(b)
    num_c = fix(c)

    total = num_a + num_b + num_c
    return render(request, "teen.html", {"form": form, "total":total})
  return render(request, "teen.html", {"form": form})


def xyz(request):
  form=Xyz(request.GET)
  if form.is_valid():
    str= form.cleaned_data['str']

    result = xyz_there(str)
    return render(request, "xyz.html", {"form": form, "str": result})
  return render(request, "xyz.html", {"form": form})



def centered(request):
  form=Average(request.GET) 
  if form.is_valid():
    num1= form.cleaned_data['num1']
    num2= form.cleaned_data['num2']
    num3= form.cleaned_data['num3']
    num4= form.cleaned_data['num4']
    num5= form.cleaned_data['num5']
    num6= form.cleaned_data['num6']
    num7= form.cleaned_data['num7']
    
    if num6 ==None and num7==None:
      nums=[num1,num2,num3,num4,num5]
    elif num6==None and num7 !=None:
      nums=[num1,num2,num3,num4,num5,num7]
    elif num6!=None and num7==None:
      nums=[num1,num2,num3,num4,num5,num6]
    elif num6!=None and num7!=None:
      nums=[num1,num2,num3,num4,num5,num6,num7]

  

    average=centered_average(nums)
    return render(request, "center.html", {"form": form, "nums": average})
  return render(request, "center.html", {"form": form})


  

  
    

