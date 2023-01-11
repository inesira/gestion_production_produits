from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Category
from app.forms import CategoryForm
from django.contrib import messages

# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    Categories = Category.objects.all()
    return render(
        request,
        'app/categories/index.html',
        {
            'Categories': Categories
        }
    )

def create(request):
    form = CategoryForm()
    return render(
        request,
        'app/categories/create.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Insertion de la categorie avec success ")
        return redirect('/category')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            Categories = Category.objects.get(pk=id)
            form = CategoryForm(instance=Categories)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form': form
            }
            )
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            Categories = Category.objects.get(pk=id)
            form = CategoryForm(request.POST,instance=Categories)
        if form.is_valid():
            form.save()
            messages.success(request," Modification de la categorie avec succes ")
        return redirect('/category')
def delete(request, id):
    Categories = Category.objects.get(pk=id)
    Categories.delete()
    messages.success(request," Suppression de la cathegorie avec succes ")
    return redirect('/category')