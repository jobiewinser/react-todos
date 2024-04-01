from django.urls import path
from . import views

urlpatterns = [
    
    # path('', HomeView.as_view(), name='home'),
    path('hello-world/', views.hello_world, name='hello_world'),
    path('todos/', views.todo_list),
    path('todos/<int:pk>/', views.todo_detail),
]