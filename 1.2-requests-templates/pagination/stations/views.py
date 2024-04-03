from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        content = [{"Name": row['Name'], "Street": row["Street"], "District": row["District"]} for row in reader]

    context = {
         'bus_stations': Paginator(content, 10).get_page(request.GET.get('page', 1)),
         'page': request.GET.get('page', 1),
    }
    return render(request, 'stations/index.html', context)
