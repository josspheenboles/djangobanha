from django.shortcuts import render

# Create your views here.
def alltrainees(req):
    return render(req,'trainee/all.html')
def add(req):
    return render(req,'trainee/add.html')
def update(req,id):
    return render(req,'trainee/update.html')
def deletetr(req,id):
    return render(req,'trainee/update.html')