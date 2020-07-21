from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

from dashboard.views import BookListView


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('books_listing/', BookListView.as_view()),
    path('book/<str:pk_test>/', views.book, name='book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
