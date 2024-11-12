from django import forms


class heyForm(forms.Form):
    name_data=forms.CharField()

class ageForm(forms.Form):
    birthyear=forms.IntegerField()
    end=forms.IntegerField()

class orderForm(forms.Form):
    burgers=forms.IntegerField()
    fries=forms.IntegerField()
    drinks=forms.IntegerField()


