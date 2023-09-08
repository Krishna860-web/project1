from django.shortcuts import render
from app2.models import tbl_stud

def index(request):
    return render(request,'index.html')

def stud(request):
    return render(request,'stud.html')

def add_details(request):
    b=tbl_stud()
    b.Name=request.POST.get('Name')
    b.Age=request.POST.get('Age')
    b.Place=request.POST.get('Place')
    b.Mark=request.POST.get('Mark')
    b.save()
    return render(request,'stud.html')

def viewstud(request):
    d=tbl_stud.objects.all()
    return render(request,'viewstud.html', {'data':d})
