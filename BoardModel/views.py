from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import BoardModel

# Create your views here.
def index(request):
    return render(request, 'BoardModel/index.html')

def list(request):
    board = BoardModel.objects.all()
    context = {
        'board' : board
    }
    return render(request, 'BoardModel/list.html', context)

def add(request):
    if request.method == 'GET':
        return render(request, 'BoardModel/add.html')
    else:
        title = request.POST['title']
        writer = request.POST['writer']
        content = request.POST['content']
        BoardModel.objects.create(title=title, writer=writer,content=content)
        return HttpResponseRedirect(reverse('BoardModel:list'))
    
def detail(request,id):
    board1 = BoardModel.objects.get(id=id)
    board1.incrementReadCount()
    con = {
        'board1' : board1
    }
    
    if request.method == 'GET':
        return render(request, 'BoardModel/detail.html', con)

def update(request,id):
    board2 = BoardModel.objects.get(id=id)
    con = {
        'board2': board2
    }
    if request.method == 'GET':
        return render(request, 'BoardModel/update.html', con)
    elif request.method == 'POST':
        title = request.POST['title']
        writer = request.POST['writer']
        content = request.POST['content']
        
        board2.title=title
        board2.writer=writer
        board2.content=content
        board2.save()
        return HttpResponseRedirect(reverse('BoardModel:list'))

def delete(request,id):
    if request.method == 'GET':
        board3 = BoardModel.objects.get(id=id)
        con = {
        'board3': board3
        }
        return render(request, 'BoardModel/delete.html', con)
    elif request.method == 'POST':        
        a = BoardModel.objects.filter(id=id)
        a.delete()
        return HttpResponseRedirect(reverse('BoardModel:list'))
