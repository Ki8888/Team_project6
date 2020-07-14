from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   
    data = {'first': 'Sanghun', 'second': 'Oh'}  #read dic
    return render(request, 'hello/home.html', context=data) 
    
