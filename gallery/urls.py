from django.urls import path

from gallery import views


urlpatterns = [
    path('gallery/', views.gallery, name='gallery')
]