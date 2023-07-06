from django.urls import path
from . import views
#for demo
from .views import calculate_shortest_distance_view

urlpatterns = [
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path("",views.home, name ='home'),
    path("index/", views.index, name='index'),
    path("parking/", views.parking, name='parking'),
    path('calculate-shortest-distance/', calculate_shortest_distance_view, name='calculate_shortest_distance'),#demo
]
