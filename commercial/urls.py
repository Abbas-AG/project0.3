
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('', views.index, name='home'),
    path('error/', views.error, name='error'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
    path('coffee/', views.coffee, name='coffee'),    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)