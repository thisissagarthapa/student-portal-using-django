from django.shortcuts import render
from .models import Students
from django.http import HttpResponse
# Create your views here.
# orm concept
def home(request):
        data=Students.objects.all()
        if request.method=='POST':
      
          return HttpResponse('successfully register')
        
        return render(request,'home.html',{'data':data})

