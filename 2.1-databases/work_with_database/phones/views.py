from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    objects = Phone.objects.all()
    sort = request.GET.get("sort")
    if sort == "min_price":
        objects = Phone.objects.order_by("price")
    elif sort == "max_price":
        objects = Phone.objects.order_by("-price")
    elif sort == "name":
        objects = Phone.objects.order_by("name")
    context = {"phones": [phone for phone in objects]
               }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        "phone": Phone.objects.filter(slug=slug).first()
    }
    return render(request, template, context)
