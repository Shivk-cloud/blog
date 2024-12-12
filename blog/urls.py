from django.urls import path
from .views import Home, post,category

urlpatterns = [
    path('Home/', Home, name='home'),  # URL for home page
    path('blog/<slug:url>/', post, name='post'),  # URL for individual post
    path('category/<slug:url>',category, name='category'),
]