from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/detail/', views.detail, name='detail'),
    path('create/', views.CreateWalk.as_view(), name='create'),
    path('people/', views.people_list, name='people_list'),
    path('people/<slug:slug>/', views.people_detail, name='people_detail'),
]
