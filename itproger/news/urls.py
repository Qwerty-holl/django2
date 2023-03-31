from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'), #http://127.0.0.1:8000/news/12/update
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),

]
