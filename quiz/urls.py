from django.urls import path
from quiz import views



urlpatterns = [
    path('quiz/', views.home, name='quiz'),

]