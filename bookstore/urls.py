from rest_framework import routers

from bookstore import views_api

app_name = 'bookstore'

router = routers.DefaultRouter()
router.register('book', views_api.BooksViewSet)
router.register('publisher', views_api.PublisherViewSet)
router.register('author', views_api.AuthorViewSet)

urlpatterns = []
urlpatterns += router.urls
