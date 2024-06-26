from django.shortcuts import render
import requests


def base(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'core/base.html',data)
