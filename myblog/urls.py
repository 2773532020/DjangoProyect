"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app_posts.views import index, post_detail, CommentCreateView  # Importamos post_detail desde app_posts.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # Definimos la ruta usando post_detail
    path('post/<int:post_id>/comment/', CommentCreateView.as_view(), name='add_comment'),
    path('comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('post/<pk>/', post_detail, name='post_detail'),  # Esto podría duplicar la ruta, revisa si es necesario
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
