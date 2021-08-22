from django.shortcuts import render , redirect 
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


# Create your views here.
def indux(request):
    todos = Task.objects.all()
    # chhal d tonobilat 3andi
    count_todos = todos.count()
    # complleted  valid 
    completed_todo = Task.objects.filter(comlete=True)
    count_completed_todo = completed_todo.count()
    # uncmpleted pas auncour 

    count_uncmpleted_todo = count_todos - count_completed_todo
    



    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            destinace = form.cleaned_data.get('destinace')
            namber_percen = form.cleaned_data.get('namber_percen')
            content  = form.cleaned_data.get('content') 
            date  = form.cleaned_data.get('date')
            data = Task(content=content ,date=date , destinace=destinace  , namber_percen=namber_percen )
            #print(data)
            form.save()
            return redirect('todoapp:homePageHotel')
    else: 
        form = TaskForm()   
   
    context = {
        'todos':todos,
        'form':form,
        'count_todos':count_todos,
        'count_completed_todo':count_completed_todo,
        'count_uncmpleted_todo':count_uncmpleted_todo,
      
    }
    #print(count_todos)
    return render(request , 'PageHomeHotel.html' , context  )


def update(request,pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=todo)
        if form.is_valid():
            #content  = form.cleaned_data.get('content' ,instance=todo) 
            #date  = form.cleaned_data.get('date' , instance=todo)
            #comlete = form.cleaned_data.get('comlete' ,instance=todo)
            #data = Task(content=content ,date=date ,comlete=comlete ,instance=todo )
            form.save()
            return redirect('todoapp:homePageHotel')

    else:
        form = TaskForm(instance=todo)
    context = {
        'form':form,

    }
    return render(request , 'update.html', context)



def delete(request , pk):
    todo = Task.objects.get(id=pk)
    if request.method== 'POST':
        todo.delete()
        return redirect('todoapp:homePageHotel') 

    return render (request ,'delete.html')