from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('posts.urls')),
    path('', include('bike.urls')),
    path('', include('orders.urls')),
    path('adminpage', views.adminpage, name='adminpage'),
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
