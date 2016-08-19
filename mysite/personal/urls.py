from django.conf.urls import url, include, patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
               #url(r'^personal/', views.personal, name='personal'),
               #url(r'^blog/', views.blog, name='blog')

               
            ]

# Create your tests here.
