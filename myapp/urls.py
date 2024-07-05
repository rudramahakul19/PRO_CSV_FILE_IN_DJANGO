from django.urls import path,include
from myapp import views

urlpatterns = [
    path('song/', views.upload, name='upload'),
]