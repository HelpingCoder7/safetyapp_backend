
from . import views
from django.urls import path,include

from .views import send_otp 

urlpatterns = [
    path("",views.home),
    path('postotp/', views.send_otp),
    path('checkotp/',views.checkotp),
    path('register/',views.register_user),
    path('loginuser/',views.loginuser),
    path('checkpg/',views.send_sms)

]