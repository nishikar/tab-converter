from django.conf.urls import patterns, url

from tab_converter import views

urlpatterns = patterns('',
    url(r'^$', views.TabConverterView.as_view(), name='base'),
)
