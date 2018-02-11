from django.shortcuts import render
from django.http import HttpResponse

from .models import Walk

# Create your views here.

def index(request):
    walks = Walk.objects.all()
    context = {'walks': walks}
    return render(request, 'walks/index.html', context)
 

