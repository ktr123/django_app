from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Category, Subcategory, location, Department
from loguru import logger
from .views import custom_api

class SubCategoryView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def validate_ids(self, location_id, department_id, category_id):
        if not location.objects.filter(location_id=location_id).exists(): 
            raise Exception(f"No Data with Location Id : {location_id}")
        if not Department.objects.filter(department_id=department_id).exists(): 
            raise Exception(f"No Data with Department Id : {department_id}")
        if not Category.objects.filter(category_id=category_id).exists(): 
            raise Exception(f"No Data with Category Id : {department_id}")


    @custom_api
    def post(self, request, *args, **kwargs):
        """
        Used for inserting Sub Category Data
        """
        location_id = kwargs.get('location_id', '')
        department_id = kwargs.get('department_id', '')
        category_id = kwargs.get('category_id', '')
        self.validate_ids(location_id, department_id, category_id)
        for row in request.data:
            row["category"] = Category(category_id=category_id)
            Subcategory(**row).save()
        return "Data Inserted in db...!!"
    

    @custom_api
    def get(self, request, *args, **kwargs):
        """
        Used for fetching sub Category Data
        """
        location_id = kwargs.get('location_id', '')
        department_id = kwargs.get('department_id', '')
        category_id = kwargs.get('category_id', '')
        self.validate_ids(location_id, department_id, category_id)
        data = list(Subcategory.objects.filter(category=category_id).all().values())
        return data


class GetSubCategoryData(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def validate_ids(self, location_id, department_id, category_id, subcategory_id):
        if not location.objects.filter(location_id=location_id).exists(): 
            raise Exception(f"No Data with Location Id : {location_id}")
        if not Department.objects.filter(department_id=department_id).exists(): 
            raise Exception(f"No Data with Department Id : {department_id}")
        if not Category.objects.filter(category_id=category_id).exists(): 
            raise Exception(f"No Data with Category Id : {category_id}")
        if not Subcategory.objects.filter(subcategory_id=subcategory_id).exists(): 
            raise Exception(f"No Data with Sub Category Id : {subcategory_id}")


    @custom_api
    def get(self, request, *args, **kwargs):
        """
        Used for fetching sub Category Data
        """
        location_id = kwargs.get('location_id', '')
        department_id = kwargs.get('department_id', '')
        category_id = kwargs.get('category_id', '')
        subcategory_id = kwargs.get('subcategory_id', '')
        self.validate_ids(location_id, department_id, category_id, subcategory_id)
        data = list(Subcategory.objects.filter(subcategory_id=subcategory_id).all().values())
        return data
