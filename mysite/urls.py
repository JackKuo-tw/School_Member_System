"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from member.views import hello_world,index,photos, gallery
from django.conf.urls import include, url
from member.dataOperation import importData,checkData
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello/$', hello_world),
    url(r'^importData/$', importData),
    url(r'^checkData/$', checkData),
    url(r'^$', index),
    url(r'^index.*?', index),
    url(r'^photos/', photos),
    url(r'^gallery/', gallery),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    
    # url(r'^upload_file/$', upload_file),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
