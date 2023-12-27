from django.urls import path
from vis import views

urlpatterns = [
    path('show/', views.show, name='showV'),
    # path('show1/', views.show1, name='show1'),

]