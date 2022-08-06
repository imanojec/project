from django.conf.urls import url
from product import views

urlpatterns=[
    url(r'^login$',views.loginApi),
    url(r'^login/([0-9]+)$',views.loginApi),
]
