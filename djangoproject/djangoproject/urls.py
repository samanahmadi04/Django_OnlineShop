"""eshop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home_models.urls')),
    path('', include('account_module.urls')),
    path('', include('article_module.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('products/', include('production.urls')),
    path('user/', include('user_panel_module.urls')),
    path('order/', include('order_module.urls')),
    path('admin/', admin.site.urls),
    path('admin-panel/', include('admin_panel.urls')),
    path('api-auth/', include('rest_framework.urls')),
]  # +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
