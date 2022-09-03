from rest_framework import serializers

from main.models import Translator, Lang


class TrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = '__all__'


class LangsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        fields = '*'
