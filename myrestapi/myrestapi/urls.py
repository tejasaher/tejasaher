"""myrestapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from geo_code import urls
#from rest_framework.authtoken import views as  authviews  # uncomment when you use basic authentication instead of JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geo_code/',include('geo_code.urls')),
    path('GetToken/',TokenObtainPairView.as_view(),name='TokenObtainPairView'),
    path('RefreshToken/',TokenRefreshView.as_view(),name='TokenRefreshView'),
    path('VerifyToken/',TokenVerifyView.as_view(),name='TokenVerifyView'),
    #path('api-auth-token/',authviews.obtain_auth_token,name='obtain_auth_token'),  ## uncomment when you use basic authentication instead of JWT
]
