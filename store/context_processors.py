from django.shortcuts import get_object_or_404, render

from .models import Category

def categories(request):
    return{
        'categories' : Category.objects.all()
    }