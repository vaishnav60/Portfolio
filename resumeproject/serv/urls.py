from django.urls import path
from . import views
urlpatterns=[
    path('accomplish/',views.accomplish,name='accomplish')
]