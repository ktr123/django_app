from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Department, Category, location
from loguru import logger
from .views import custom_api

class CategoryView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def validate_ids(self, location_id, department_id):
        if not location.objects.filter(location_id=location_id).exists(): 
            raise Exception(f"No Data with Location Id : {location_id}")
        if not Department.objects.filter(department_id=department_id).exists(): 
            raise Exception(f"No Data with Department Id : {department_id}")


    @custom_api
    def post(self, request, *args, **kwargs):
        """
        Used for inserting Category Data
        """
        location_id = kwargs.get('location_id', '')
        department_id = kwargs.get('department_id', '')
        self.validate_ids(location_id, department_id)
        kwargs.get('category_id', '')
        for row in request.data:
            row["department"] = Department(department_id=department_id)
            Category(**row).save()
        return "Data Inserted in db...!!"
    

    @custom_api
    def get(self, request, *args, **kwargs):
        """
        Used for fetching Sub Category Data
        """
        location_id = kwargs.get('location_id', '')
        department_id = kwargs.get('department_id', '')
        self.validate_ids(location_id, department_id)
        data = list(Category.objects.filter(
            department=department_id).all().values())
        return data
