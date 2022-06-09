from django.contrib import admin
from django.urls import path,include
from library import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile_view,name='profile'),
    path('delete/<int:pk>',views.delete_data,name='delete'),
    path('update/<int:pk>',views.update_books,name='update'),
    path('logout/',views.logout_view,name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
