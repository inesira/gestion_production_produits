from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Category


def index(request):
    assert isinstance(request, HttpRequest)
    Categories = Category.objects.all()
    return render(
        request,
        'app/categories_resp/index.html',
        {
            'Categories': Categories
        }
    )