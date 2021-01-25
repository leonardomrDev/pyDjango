from django.shortcuts import render
from address.forms import AddressForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AddressForm

def index(request):
    form = AddressForm()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

#def cadastro(request):
 #   if request.method == 'POST':
  #      form = AddressForm (request.POST)
   #     contexto = {'form':form}
    #    return render(request, 'cadastro.html', contexto)

def cadastro(request):
 if request.method == 'GET':
    form = AddressForm()
    contexto = {'form':form}
    return render(request, 'cadastro.html', contexto)

def GetForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddressForm()

    return render(request, 'cadastro.html', {'form': form})