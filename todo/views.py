from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Todo
# Create your views here.
#y=todo.objects.all()
def allview(request): 
	y=Todo.objects.all().order_by('-time_added')
	return render(request,'index.html',{'todo':y})
def addtodo(request):
    if request.method == 'POST':
        x = request.POST['content']
        new_item=Todo(content=x)
        new_item.save()
        return HttpResponseRedirect('/') 
    else:
        redirect('alltodoview')