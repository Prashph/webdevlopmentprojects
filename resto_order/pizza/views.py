from django.forms import formset_factory
from django.shortcuts import render
from .forms import PizzaForm
from .models import Pizza


def home(request):
    templates = "pizza/home.html"
    return render(request, templates)


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Thanks for ordering! Your %s %s and %s pizza on its way!' % (filled_form.cleaned_data['size'],
                                                                                 filled_form.cleaned_data['topping1'],
                                                                                 filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, "pizza/order.html", {'created_pizza_pk': created_pizza_pk, 'pizzaform': new_form, 'note': note})
        else:
            form = PizzaForm
            return render(request, "pizza/order.html", {'pizzaform': form})

    form = PizzaForm
    return render(request, "pizza/order.html", {'pizzaform': form})

def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'pizza/edit_order.html', {'note': note, 'pizzaform': form, 'pizza': pizza})
    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza})
