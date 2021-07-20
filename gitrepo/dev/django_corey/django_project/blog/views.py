from django.shortcuts import render
from . models import Post
# from django.http import HttpResponse

posts =[ 
  {'author':'Mukibi Joseph',
   'title':'Blog post 1',
   'content':'First post content',
   'date_posted':'August 27,2020'
	},
  {
   'author':'Mukibi Joseph',
   'title':'Blog post2',
   'content':'Second post content',
   'date_posted':'December 27,2020'
	}
]


def home(request):
	
	return render(request,'blog/home.html', {'m':Post.objects.all()})


def about(request):
	return render(request, 'blog/about.html',{'title':'About'})
