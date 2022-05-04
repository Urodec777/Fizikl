from django.http import JsonResponse
from django.shortcuts import render
import datetime
""" rendering index page with form """
def index(request):
    return render(request, 'index.html')

""" function to define number of week """
def ajax(request):
# date splitting to convert data in integer because datetime.date works with integer!
    date = request.GET['date'].split('/')
    year = int(date[-1])
    month = int(date[1])
    day = int(date[0])
    if year >= 2019:
        number_of_week = datetime.date(year=year, month=month, day=day).strftime('%U')
        return JsonResponse(number_of_week, safe=False)
    else:
        # raising ValueError to switch from "success" to "error" case
        raise ValueError
