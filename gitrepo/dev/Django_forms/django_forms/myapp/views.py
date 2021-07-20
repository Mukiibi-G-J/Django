
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm
 

def  contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email= form.cleaned_data['email']
            
            print(name, email)
                
    
    form = ContactForm()
    return render(request,'forms.html',{'form':form})

def snippet_details(request):
     if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            print('vald')



        form =SnippetForm()
        return render(request,'forms.html',{'form':form}) 