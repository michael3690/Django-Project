from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('posts/', views.posts.as_view(), name='posts'),
    path('add_content/', views.content, name='add_content'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name='index'),
]