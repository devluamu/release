from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^payment$', views.payment, name='payment'),
    url(r'^event$', views.event, name='event'),
    url(r'^notice$', views.notice, name='notice'), 
]
