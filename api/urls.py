from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('blogposts/',views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('blogposts/<slug:slug>/',views.BlogPostDetail.as_view(),name='blogpost-view-delete'),
    path('blogposts/me/', views.MyBlogPostList.as_view(), name='my-posts'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<slug:slug>/',views.CategoryDetail.as_view(),name='category-view-delete'),
]