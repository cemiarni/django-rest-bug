"""bug URL Configuration

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
from rest_framework import routers, serializers, viewsets, fields

from bug.models import IP


class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IP
        fields = '__all__'


class IP2Serializer(serializers.ModelSerializer):
    class Meta:
        model = IP
        fields = '__all__'

    ipv4 = fields.IPAddressField(protocol='ipv4')
    ipv6 = fields.IPAddressField(protocol='ipv6')
    both = fields.IPAddressField()


class IpViewSet(viewsets.ModelViewSet):
    serializer_class = IPSerializer
    queryset = IP.objects.all()


class Ip2ViewSet(viewsets.ModelViewSet):
    serializer_class = IP2Serializer
    queryset = IP.objects.all()

router = routers.DefaultRouter()
router.register(r'bug', IpViewSet)
router.register(r'workaround', Ip2ViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
