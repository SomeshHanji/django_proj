from django.shortcuts import render
from django.template.context_processors import request

from .models import Venue
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date


def database(request):
    t = date.today()
    m = date.strftime(t, '%b')
    y = t.year
    title = "Myclub Events calender -%s %s" % (m, y)
    return HttpResponse("<h1>%s</h1>" % title)


def database1(request):
    t = date.today()
    m = date.strftime(t, '%b')
    y = t.year
    title = "Myclub Events calender -%s %s" % (m, y)
    return HttpResponse("<h1 style='color:yellow;background-color:blue;text-align:center> %s </h1>" % title)


def base(request):
    if request.method == "POST":
        form_list = venue(request.POST)
        if form_list.is_valid():
            form_list.save()
            return HttpResponseRedirect('/')

    else:
        form_list = venue()

    if request.method == "POST":
        form_item = venue(request.POST)
        if form_item.is_valid():
            form_item.save()
            return HttpResponseRedirect('/')

    else:
        form_item = venue()

    # grap all TodoItems from database:
    all_todos = venue.objects.all()

    # grap all TodoLists (titles) from database:
    titles = venue.objects.all()

    return render(request, 'edit.html',
                  {
                      'form_list': form_list,
                      'form_item': form_item,
                      'all_todos': all_todos,
                      'titles': titles
                  })


# def index(request):
#     name="Nishant Totar"
#     context={
#         'name':name
#     }
#     return render(request, 'index.html',context=context)
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    return render(request, 'cal.html', {'title': title, 'cal': cal})
