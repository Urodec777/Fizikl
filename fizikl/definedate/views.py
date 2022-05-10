from django.views.generic import TemplateView
from .serializers import DateSerializer
from django.shortcuts import render
import datetime
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

""" rendering index page with form """


class Index(TemplateView):
    template_name = 'index.html'


class DateView(GenericAPIView):

    def get(self, request):
        try:
            serializer = DateSerializer(data={'date': request.GET['date']})
        except:
            # this line of code to prevent 500 error when user comes to /ajax/ in DRF
            serializer = DateSerializer(
                data={'date': datetime.datetime.now().strftime('%d / %m / %Y')})
        # getting datetime instance of selected date to check year
        date = datetime.datetime.strptime(
            serializer.initial_data.get('date'), '%d / %m / %Y')
        if serializer.is_valid(raise_exception=True) and date.year >= 2019:
            return Response(data=serializer.validated_data.get('date').strftime('%U'))
