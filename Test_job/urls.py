"""Test_job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.User.views import update_profile
from Test_job import settings
from apps.Cards.views import CardListView, CardDetailView, IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('cards/', CardListView.as_view(), name='index_cards'),
    path('cards/<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/edit/<int:pk>/', update_profile, name='user_edit'),
    path('categories/<int:pk>/', CardListView.as_view(), name='category_detail')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
