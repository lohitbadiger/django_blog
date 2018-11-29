from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# posts=[

#     {
#         'author': 'lohit',
#         'title':'Sun',
#         'content':'Lorem ipsum dolor sit ame',
#         'age': 37,
#         'topic': 'Sci-fic',
#         'date_posted': '09 sep 2017'
#     },
#       {
#         'author': 'Takuma',
#         'title':'Moon',
#         'content':'Lorem ipsum dolor sit ame',
#         'age': 37,
#         'topic': 'Sci-fic',
#         'date_posted': '10 sep 2017'
#     }

# ]
# def home(request):
#     return HttpResponse('<h1> Blog Home</h1>')


def home(request):
    context={
        # 'posts':posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

