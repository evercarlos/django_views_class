from django.conf.urls import url
from .views import CompanyView
from django.urls import path

urlpatterns = [
     url(r'^companies$',CompanyView.as_view()),
     path('companies/<int:id>',CompanyView.as_view(),name='companies_process')
     #url(r'^companies/(?P<id>\w+)/$',CompanyView.as_view()),
]
