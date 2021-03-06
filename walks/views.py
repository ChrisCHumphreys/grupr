from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View


from .models import Walk, People
from .forms import WalkForm

# Create your views here.

def index(request):
    walks = Walk.objects.all()
    context = {'walks': walks}
    return render(request, 'walks/index.html', context)

def detail(request, slug):
    walk = get_object_or_404(Walk, slug=slug)
    return render(request, 'walks/detail.html', {'walk' : walk})

class CreateWalk(View):
    form_class = WalkForm
    template_name = 'walks/walk_create.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form':self.form_class(initial = {'slug': ' '})})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            new_object.save()
            return redirect(new_object)
        else:
            return render(
                request,
                self.template_name,
                {'form':bound_form})

def people_list(request):
    people = People.objects.all()
    context = {'people': people}
    return render(request, 'walks/people_list.html', context)

def people_detail(request, slug):
    person = get_object_or_404(People, slug=slug)
    return render(request, 'walks/person_detail.html', {'person':person})

'''
def create_walk(request):
    return HttpResponse("Create is live")
'''

