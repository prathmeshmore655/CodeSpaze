from .models import ModelDataTables
from rest_framework import serializers

class ModelDataTableSerializer (serializers.ModelSerializer):

    class Meta:

        model = ModelDataTables

        fields = '__all__'