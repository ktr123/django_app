from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Category, Subcategory, location, Department, Sku
from loguru import logger
from .views import custom_api

class SkuView(APIView):
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
    def post(self, request, *args, **kwargs):
        """
        Used for storing sku data
        """
        for row in request.data:
            location_id = row.get('location', '')
            department_id = row.get('department', '')
            category_id = row.get('category', '')
            subcategory_id = row.get('subcategory', '')
            self.validate_ids(location_id, department_id, category_id, subcategory_id)
            row["location"] = location(location_id=location_id)
            row["department"] = Department(department_id=department_id)
            row["category"] = Category(category_id=category_id)
            row["subcategory"] = Subcategory(subcategory_id=subcategory_id)
            Sku(**row).save()
        return "Data Updated in db...!!"
    
    @custom_api
    def get(self, request):
        """
        Used for fetching sku data with location,
        category,dept and sub category values
        """
        data = []
        for row in list(Sku.objects.all().values()):
            location_val = location.objects.filter(location_id=row['location_id']).all().values('name')[0]['name']
            category_val = Category.objects.filter(category_id=row['category_id']).all().values('category_name')[0]['category_name']
            department_val = Department.objects.filter(department_id=row['department_id']).all().values('department_name')[0]['department_name']
            subcategory_val = Subcategory.objects.filter(subcategory_id=row['subcategory_id']).all().values('subcategory_name')[0]['subcategory_name']
            data.append({
                "sku_name": row["sku_name"],
                "sku_id": row["sku_id"],
                "location_val": location_val,
                "category_val": category_val,
                "department_val": department_val,
                "subcategory_val": subcategory_val
            })
        return data

