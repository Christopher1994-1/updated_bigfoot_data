from django.urls import path
from . import views





urlpatterns = [
    path('', views.index1, name='index1'),
    path('state_selection/<str:state_name>/', views.state_selection, name="state_selection")
]
