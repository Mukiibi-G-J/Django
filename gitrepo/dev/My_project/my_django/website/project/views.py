from django.shortcuts import render


def home (request):
	return render (request, 'index.html')

def mattress (request):
    return render(request, 'mattress.html')