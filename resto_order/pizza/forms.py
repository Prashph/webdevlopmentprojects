from django import forms
from .models import Pizza, Size


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(max_length=100)
#     topping2 = forms.CharField(max_length=100)
#     size = forms.ChoiceField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        lebals = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}



