from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.calorie_list, name='calorie_list'),
    path('add/', views.add_calorie, name='add_calorie'),
    
]