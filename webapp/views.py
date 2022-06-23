from django.shortcuts import render


def index_view(request):
    context = {"test": 'TEST'}
    return render(request, 'index.html', context)
