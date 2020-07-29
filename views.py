from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def Todoview(request):
   all_todo_items = TodoItem.objects.all()
   return render(request, 'todo.html', 
   {'all_items' : all_todo_items})

def addTodo(request):
    
    #create a new todo all_items
    request.POST['content']
    new_item = TodoItem(content = request.POST['content'] )
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
   items_to_del =  TodoItem.objects.get(id = todo_id)
   items_to_del.delete()
   return HttpResponseRedirect('/todo/')


