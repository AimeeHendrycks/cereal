"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #url(pattern, view)
    url(r'^cereal_list/$', 'main.views.cereal_list'),
    url(r'^cereal_detail/(?P<pk>\d+)/$', 'main.views.cereal_detail'),
    url(r'^cereal_search/$', 'main.views.cereal_search'),
    url(r'^cereal_create/$', 'main.views.cereal_create'),
    url(r'^cereal_update/$', 'main.views.cereal_update'),
    url(r'^cereal_update_spec/', 'main.views.cereal_update_spec'),
    url(r'^cereal_delete/$', 'main.views.cereal_delete'),
    url(r'^manufacturer_list/$', 'main.views.manufacturer_list'),
    url(r'^manufacturer_detail/(?P<pk>\d+)/$', 'main.views.manufacturer_detail'),
    url(r'^manufacturer_search/$', 'main.views.manufacturer_search'),
    url(r'^manufacturer_create/$', 'main.views.manufacturer_create'),
    url(r'^manufacturer_update/$', 'main.views.manufacturer_update'),
    url(r'^manufacturer_update_spec/$', 'main.views.manufacturer_update_spec'),
    url(r'^manufacturer_delete/$', 'main.views.manufacturer_delete'),
    url(r'^base/$', 'main.views.base'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#(.*\.txt$)