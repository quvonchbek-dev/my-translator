from rest_framework import serializers

from main.models import Translator, Lang


class TrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = '__all__'

