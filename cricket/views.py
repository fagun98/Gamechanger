from django.shortcuts import render

from .models import formation
from .forms import formationForm

def index(request):
    return render(request, 'cricket/index.html')

def formation(request):
    form = formationForm(request.POST or None)
    if form.is_valid():
        new_formation = form.save()
        form = formationForm()
        print(new_formation.pk)
    context = {
        'form':form
    }


    return render(request,'cricket/formation.html',context)

