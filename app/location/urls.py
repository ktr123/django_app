from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from location.RegisterAPIView import RegisterAPIView, LogoutView
from location.views import test
from location.department import DepartmentView
from location.location import LocationView
from location.category import CategoryView
from location.sub_category import SubCategoryView, GetSubCategoryData
from location.sku import SkuView


urlpatterns = [
    path('test',
         test,
         name='test'),
        path('login/',
         TokenObtainPairView.as_view(),
         name='token_obtain'),
    path('token_refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('register_user/',
         RegisterAPIView.as_view(),
         name='Register'),
    path('logout/',
         LogoutView.as_view(),
         name='Logout'),
    re_path(r'^api/v1/location/(?P<location_id>[0-9A-Za-z]+)/department/(?P<department_id>[0-9A-Za-z]+)/category/(?P<category_id>[0-9A-Za-z]+)/subcategory/(?P<subcategory_id>[0-9A-Za-z]+)',
            GetSubCategoryData.as_view(),
            name='subcategory'),
    re_path(r'^api/v1/location/(?P<location_id>[0-9A-Za-z]+)/department/(?P<department_id>[0-9A-Za-z]+)/category/(?P<category_id>[0-9A-Za-z]+)/subcategory',
            SubCategoryView.as_view(),
            name='subcategory'),
    re_path(r'^api/v1/location/(?P<location_id>[0-9A-Za-z]+)/department/(?P<department_id>[0-9A-Za-z]+)/category$',
            CategoryView.as_view(),
            name='category'),
    re_path(r'^api/v1/location/(?P<location_id>[0-9A-Za-z]+)/department$',
            DepartmentView.as_view(),
            name='department'),
    re_path(r'api/v1/location',
            LocationView.as_view(),
            name='location'),
    path(r'api/v1/sku',
            SkuView.as_view(),
            name='location'),
]