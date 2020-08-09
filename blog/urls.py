from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:pk>',views.detail,name='detail'),
    path('categories/<int:pk>/',views.category,name='category'),
    path('search/', views.search, name='search'),
    path('archive/',views.archive,name='archive'),
    path('about/',views.about,name='about'),
]