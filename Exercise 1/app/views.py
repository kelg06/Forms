from django.shortcuts import render
from app.forms import *

# Create your views here.
def hey(request):
    form = heyForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name_data"]
        hey_name=f'Hey, {name}!'
        return render(request,"hey.html",{"form":form,"hey":hey_name})
    
    return render(request,"hey.html",{"form":form})

def age(request):
    form=ageForm(request.GET)
    if form.is_valid():
        birthyear=form.cleaned_data["birthyear"]
        end=form.cleaned_data["end"]
        answer=end-birthyear
        return render(request,"age.html",{"form":form, "answer":answer})
    
    return render(request,"age.html",{"form":form})


def order(request):
    form=orderForm(request.GET)
    if form.is_valid():
        burgers=form.cleaned_data["burgers"]
        fries=form.cleaned_data["fries"]
        drinks=form.cleaned_data["drinks"]
        burg_tot= int(burgers) *4.50
        fri_tot=int(fries)*1.50
        dri_tot=int(drinks)*1.00
        total=burg_tot+dri_tot+fri_tot
        return render (request,"order.html",{"form":form, "total":total})
    
    return render(request,"order.html",{"form":form})


