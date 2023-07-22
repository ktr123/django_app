from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from .models import  location
from loguru import logger
from .views import custom_api

class LocationView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @custom_api
    def post(self, request):
        """
        Used for inserting Location Data
        """
        body_data = request.data
        for row in body_data:
            location(**row).save()
        return "Data Inserted in db...!!"
    
    @custom_api
    def get(self, request):
        """
        Used for fetching Location Table Data
        """
        return list(location.objects.all().values())