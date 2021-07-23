from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    # dynamic url routing
    path('post/<str:pk>', views.posts, name='post')

]
