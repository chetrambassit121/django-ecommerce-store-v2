from django.shortcuts import render
from ecommerce.inventory import models


def home(request):

    return render(request, "index.html")


def category(request):

    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):

    # x = models.Product.objects.filter(category__name="fashion")
    # print(models.Product.objects.filter(category__name="fashion").explain(verbose=True, analyze=True))

    y = (
        models.Product.objects.filter(category__name=category)
        .filter(product__is_default=True)
        .values("id", "name", "slug", "created_at", "category__name", "product__store_price")
    )

    # data = serializers.serialize("json", x, indent=4)

    return render(request, "product_by_category.html", {"data": y})
