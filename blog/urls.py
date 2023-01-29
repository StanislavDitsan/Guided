from . import views
from django.urls import path
from .views import CategoryView, search, delete_comment

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.PostList.as_view(), name='blog'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>/update',
         views.UpdatePostView.as_view(),
         name='update_post'),
    path('post/<int:pk>/delete',
         views.DeletePostView.as_view(),
         name='delete_post'),
    path('category/<str:category>/', CategoryView, name='category'),
    path('search', views.search, name='search'),
    path('post/<int:pk>/delete/',
         views.delete_comment,
         name='delete_comment'),
]