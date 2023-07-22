from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Department, location
from loguru import logger
from .views import custom_api

class DepartmentView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def validate_location_id(self, location_id):
        if not location.objects.filter(location_id=location_id).exists(): 
            raise Exception(f"No Data with Location Id : {location_id}")


    @custom_api
    def post(self, request, *args, **kwargs):
        """
        Used for inserting Department Data
        """
        location_id = kwargs.get('location_id', '')
        self.validate_location_id(location_id)
        for row in request.data:
            row["location"] = location(location_id=location_id)
            Department(**row).save()
        return "Data Inserted in db...!!"
    

    @custom_api
    def get(self, request, *args, **kwargs):
        """
        Used for fetching Department Data
        """
        location_id = kwargs.get('location_id', '')
        self.validate_location_id(location_id)
        data = list(Department.objects.filter(
            location=location_id).all().values())
        return data
