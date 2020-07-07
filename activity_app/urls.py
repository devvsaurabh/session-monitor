from django.conf.urls import url
from activity_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]