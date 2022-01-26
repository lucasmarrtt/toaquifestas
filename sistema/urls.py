"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static  
from django.conf import settings  

from home.views import get_json_car_data, get_json_model_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), 
    path('', include('pwa.urls')), 
    path('chaining/', include('smart_selects.urls')),

    path('cars-json/', get_json_car_data, name='cars-json'),
    
    path('models-json/<str:car>/', get_json_model_data, name='models-json'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.AdminSite.site_header = 'Sistema de gerenciamento Nexxt'
admin.AdminSite.site_title = 'Sistema de gerenciamento Nexxt'
admin.AdminSite.index_title = 'Painel Nexxt'