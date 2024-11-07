from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import ModelDataTables
from .serializers import ModelDataTableSerializer
from rest_framework.decorators import api_view


class ProductList(APIView):

    def get(self, request , pk = None):
        data = ModelDataTables.objects.all()
        serialized_data = ModelDataTableSerializer(data, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = ModelDataTableSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = ModelDataTables.objects.get(pk=pk)
        except ModelDataTables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_data = ModelDataTableSerializer(user, data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = ModelDataTables.objects.get(pk=pk)
        except ModelDataTables.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
