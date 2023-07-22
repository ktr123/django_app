from django.db import models

class location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location_description = models.TextField()

    def __str__(self):
        return self.location_name

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    location = models.ForeignKey(location,on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.department_name

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.category_name
    

class Subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.subcategory_name


class Sku(models.Model):
    sku_id = models.IntegerField(primary_key=True)
    sku_name = models.CharField(max_length=255)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
