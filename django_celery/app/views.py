from django.shortcuts import render

from django_celery.celery import add


# Create your views here.
def Home(request):
    result = add.delay(1, 2)
    print("result", result)
    return render(request, 'app/home.html')
