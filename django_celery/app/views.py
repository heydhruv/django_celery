from celery.result import AsyncResult
from django.shortcuts import render

from app.task import add, sub


# Create your views here.
def Home(request):
    result1 = add.apply_async(args=[10, 20])
    result2 = sub.apply_async(args=[80, 10])
    return render(request, 'app/home.html', {"add": result1, "sub": result2})

