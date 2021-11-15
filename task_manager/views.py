from django.shortcuts import render


def index(request):
    context = {'who': 'World'}
    return render(request, 'index.html', context)