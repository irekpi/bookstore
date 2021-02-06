from django.urls import path
from rest_framework import routers

from bookstore import views_api

app_name = 'bookstore'

router = routers.DefaultRouter()
router.register('book', views_api.BooksViewSet)
router.register('publisher', views_api.PublisherViewSet)
router.register('author', views_api.AuthorViewSet)

urlpatterns = [
    path('book/<book_id>/', views_api.BookView.as_view(), name='book_detail'),
    path('publisher/<publisher_id>/', views_api.PublisherDetailView.as_view(), name='publisher_detail'),
    path('author/<author_id>/', views_api.AuthorDetailView.as_view(), name='author_detail'),
]
urlpatterns += router.urls
