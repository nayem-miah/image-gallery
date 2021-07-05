from django.shortcuts import render
from .models import *



def index(request):
    template = 'index.html'
    category = Catagory.objects.all()
    gallry = Photo.objects.all()
    context={
        'category':category,
        'gallery':gallry,
    }
    
    return render(request, template_name=template, context=context)



def add(request):

    template = 'add.html'
    category = Catagory.objects.all()

    context={

        'category':category,

    }

    return render(request,template_name=template, context=context)


def view(request, pk):
    template = 'view.html'
    gallry = Photo.objects.get(id=pk)
  
    context={

        'views':gallry
    }
    return render(request, template_name=template,context=context)
