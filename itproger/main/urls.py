from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('about', views.about, name='about'),
                  path('contact', views.contact, name='contact'),
                  path('login', views.MyprojectLoginView.as_view(), name='login'),
                  path('register', views.RegisterUserView.as_view(), name='register'),
                  path('logout', views.MyProjectLogout.as_view(), name='logout'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
