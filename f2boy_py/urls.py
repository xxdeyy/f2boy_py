"""f2boy_py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from apps.homepage.views import homepage
from apps.wife.views import wife
from f2boy_py import settings

admin.autodiscover()

urlpatterns = [
    url(r'^$', homepage),
    url(r'^poem/', include('apps.poem.urls')),
    url(r'^message/', include('apps.message.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^wechat/', include('apps.wechat.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^wife/', wife),
    # url(r'^favicon.ico$', RedirectView.as_view(url='http://odwsp46yw.bkt.clouddn.com/images/favicon.ico')),
]
