from rest_framework import serializers
class DateSerializer(serializers.Serializer):
    date = serializers.DateField(format='%d / %m / %Y', input_formats=['%d / %m / %Y'])