from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('post/', views.check_boardnum, name='check_num'),

]
