from geo_code import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('get/',views.get_geo_code,name='get_geo_code'),
    path('create/',views.create_geo_code,name='create_geo_code'),
    path('update/<str:pk>/',views.update_geo_code,name='update_geo_code'),
    path('delete/<str:pk>/',views.delete_geo_code,name='delete_geo_code'), #str:pk to pass pk in url to update records for eg seo_id is primary key 
    
    ]
