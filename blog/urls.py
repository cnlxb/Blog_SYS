from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:pk>',views.detail,name='detail'),
    path('categories/<int:pk>',views.category,name='category'),
    path('tags/<int:pk>',views.tag,name='tags'),
    path('archives/<int:year>/<int:month>/',views.archive,name='archive'),
    path('about',views.about,name='about'),
    path('search',views.search,name='search')
]