from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Yoooooooooooooo</h1>')

def detail(request, Question_id):
    return HttpResponse('This is the detail view of the question %s'% Question_id)
def results(request, Question_id):
    return HttpResponse('There are the results of the question %s' % Question_id)