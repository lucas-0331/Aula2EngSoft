from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')


def view(request):
    return render(request, 'index.html')