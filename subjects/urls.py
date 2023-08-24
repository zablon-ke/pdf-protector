from django.urls import path
from . import views

urlpatterns=[
    path("/subjects",views.index,name='subjects')
]