from django import forms

class FrontTimes(forms.Form):
    string = forms.CharField()
    number = forms.IntegerField()

class FixTeen(forms.Form):
    a= forms.IntegerField()
    b =forms.IntegerField()
    c=forms.IntegerField()
    

class Xyz(forms.Form):
    str=forms.CharField()

class Average(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()
    num3=forms.IntegerField()
    num4=forms.IntegerField()
    num5=forms.IntegerField()
    num6=forms.IntegerField(required=False)
    num7=forms.IntegerField(required=False)
