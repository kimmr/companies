from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.company_detail, name="company-detail")
]
