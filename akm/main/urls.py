from django.conf.urls import url
from akm.main import views

urlpatterns = [
        url(r'^$', views.index, name = "main"),
]