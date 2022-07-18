from django.shortcuts import render
from ecommerce.inventory import models


def home(request):

    return render(request, "index.html")
