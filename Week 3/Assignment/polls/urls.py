from django.urls import path
from polls import views
app_name = 'polls'
urlpatterns = [
    path('owner/', views.owner, name='owner'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
]