"""drf_boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from post.views import PostViewSet, CommentViewSet

post_router = SimpleRouter()
post_router.register(r'', PostViewSet)

comment_router = SimpleRouter()
comment_router.register(r'', CommentViewSet, base_name='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/post/', include(post_router.urls)),
    url(r'^api/v1/comment/', include(comment_router.urls)),
]
