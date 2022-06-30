from django.contrib import admin
from django.urls import path
from books import views

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/",views.show_books,name='books'),
    path("upload_books/",views.upload_book,name='upload_book'),
    path('update_book/<int:pk>/',views.update_book,name='update-book'),
    path("delete_book/<int:pk>",views.delete_book,name='delete-book'),
    path("detail_book/<int:pk>",views.get_detail,name='detail-book'),
    path('student/<slug:abc12_12-12345-8>')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
