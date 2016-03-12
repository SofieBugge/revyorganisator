from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ovedag/(?P<øvedag_dato_url>\w+)/$', views.øvedag, name='øvedag'),
]
