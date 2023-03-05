from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
]