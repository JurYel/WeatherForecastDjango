from django.urls import path
from forecast import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    
]