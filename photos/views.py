from django.shortcuts import redirect, render
from .models import *


def index(request):
    template = 'index.html'

    # we get exect category name by categ which is used in html file
    cate = request.GET.get('categ')
    if cate == None:  # if we category name not found

        gallry = Photo.objects.all()

    else:
        gallry = Photo.objects.filter(
            catagory__name=cate)  # if category name found then it will filter. "catagory__name" here catagory is a object of Photo class and catagory is also forign key of Catagory class. So catagory object means Catagory class and Catagory class has a name object that's how " catagory__name" works

    category = Catagory.objects.all()

    context = {
        'categories': category,
        'gallery': gallry,
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

        if data['category'] != 'none':  # if work when u select a category that already exixts
            # by 'id=data['category'] we bring our exact category id
            category = Catagory.objects.get(id=data['category'])
        # it works when u create a new category
        elif data['new_category'] != '':
            # here created variable is default. 'get_or_create' will create a category and bring the category from database once time
            category, created = Catagory.objects.get_or_create(
                name=data['new_category'])
        else:
            category = None  # it works when u select neither existing category nor new category

        photo = Photo.objects.create(
            photo=imag['im'], catagory=category, description=data['description'])

        return redirect('index')

    context = {

        'category': category,

    }

    return render(request, template_name=template, context=context)


def view(request, pk):
    template = 'view.html'
    gallry = Photo.objects.get(id=pk)

    context = {

        'views': gallry
    }
    return render(request, template_name=template, context=context)
