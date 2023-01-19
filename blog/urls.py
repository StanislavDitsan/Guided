from . import views
from django.urls import path

urlpatterns = [
    path('blog', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('home', views.home, name='home'),
]