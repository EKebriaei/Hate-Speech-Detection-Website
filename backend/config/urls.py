"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions

from forum.views import MessageViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api-docs/', include_docs_urls(title='Forum App API',  permission_classes=(permissions.AllowAny,))),
    re_path(r'^api-auth/', include('djoser.urls')),
    re_path(r'^api-auth/', include('djoser.urls.authtoken')),
    re_path(r'^api/', include(router.urls)),
]