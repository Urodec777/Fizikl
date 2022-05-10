# from django.http import JsonResponse
from .serializers import DateSerializer
from django.shortcuts import render
import datetime
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

""" rendering index page with form """
def index(request):
    return render(request, 'index.html')

""" function to define number of week """
# def ajax(request):
# # date splitting to convert data in integer because datetime.date works with integer!
#     date = request.GET['date'].split('/')
#     year = int(date[-1])
#     month = int(date[1])
#     day = int(date[0])
#     if year >= 2019:
#         number_of_week = datetime.date(year=year, month=month, day=day).strftime('%U')
#         return JsonResponse(number_of_week, safe=False)
#     else:
#         # raising ValueError to switch from "success" to "error" case
#         raise ValueError

class DateView(GenericAPIView):

    def get(self, request):
        try:
            serializer = DateSerializer(data={'date': request.GET['date']})
        except:
            # this line of code to prevent 500 error when user comes to /ajax/ in DRF
            serializer = DateSerializer(data={'date': datetime.datetime.now().strftime('%d / %m / %Y')})
        # getting datetime instance of selected date to check year
        date = datetime.datetime.strptime(serializer.initial_data.get('date'), '%d / %m / %Y')
        if serializer.is_valid(raise_exception=True) and date.year >= 2019:
            return Response(data = serializer.validated_data.get('date').strftime('%U'))
