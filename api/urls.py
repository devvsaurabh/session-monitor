from django.urls import path
from api import views



urlpatterns = [
    path('users/',views.users),
    path('userdata/<str:c_id>',views.userdata),
    path('delete/<str:c_id>',views.delete),
    path('update/',views.update),
]


