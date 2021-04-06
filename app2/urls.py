from django.urls import path
from app2 import views

app_name="app2"

urlpatterns=[
    path('',views.index,name="index"),
    path("app2/",views.sample2,name="app2"),
    path("sam2/",views.sample_app2,name="sample2"),
]