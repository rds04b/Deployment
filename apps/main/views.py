from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'main/index.html', context)

def create(request):
    if request.method =='POST':
        valid, data = Course.objects.validate_and_create(request.POST)

        if valid:
            print "Successful Entry!"
        else:
            for err in data:
                messages.error(request, err)

    return redirect('main:index')

def confirm(request, id):
    context = {
        "courses" : Course.objects.get(id=id)
    }
    return render(request, "main/remove.html", context)


def remove(request, id):
    request.method =='POST'
    Course.objects.filter(id=id).delete()
    return redirect('main:remove')
