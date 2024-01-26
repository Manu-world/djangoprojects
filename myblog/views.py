from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

# Create your views here.

def listView(request):
    template ='index.html'
    context = {}

    todos = Todo.objects.all

    context['todos']= todos

    return render(request, template, context)
