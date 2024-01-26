from django.shortcuts import render, HttpResponseRedirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def listView(request):
    template ='index.html'
    context = {}

    todos = Todo.objects.all

    context['todos']= todos

    return render(request, template, context)

def createView(request):
    template = 'create_todo.html'
    context = {}

    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    
    context['form']=form

    return render(request, template, context)

def deleteView(request, pk):
    template='delete.html'
    context={}

    todo = Todo.objects.get(id=pk)

    if request.method =='POST':
        todo.delete()
        return HttpResponseRedirect('/')

    context['todo']=todo

    return render(request, template, context)

