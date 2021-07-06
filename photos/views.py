from django.shortcuts import redirect, render
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
    
    if request.method == 'POST':
        data = request.POST  
        imag = request.FILES
        # "data = request.POST" by this code we can grab all data
        # "img = request.FILES" by this code we can grab all image
        # "data = request.POST.get('description')" by this code we can grab only description data nothing more
        # "img = request.FILES.get('image')" by this code we can grab only image's picture data nothing more
       
        if data['category'] != 'none':      #if work when u select a category that already exixts
            category = Catagory.objects.get(id = data['category'])        #by 'id=data['category'] we bring our exact category id
        elif data['new_category'] != '':                                 # it works when u create a new category
            category, created = Catagory.objects.get_or_create(name=data['new_category'])              # here created variable is default. 'get_or_create' will create a category and bring the category from database once time
        else: 
            category = None                                      #it works when u select neither existing category nor new category
        
        photo = Photo.objects.create(photo = imag['im'],catagory = category,description=data['description'])
        
        return redirect('index')



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
