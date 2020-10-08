from django.shortcuts import render

# Create your views here.

def mdb_view(request):
    return render(request,'mdb.html')


def temp(request):
    return render(request,'temp.html')