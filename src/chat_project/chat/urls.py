from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.chat_page, name='chat_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)