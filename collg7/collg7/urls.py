from django.contrib import admin
from django.urls import path
from poll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('home/<int:pk>',views.detail_home,name='detail'),

    path('index/',views.index,name='index'),
    path('page/',views.page,name='page'),
]
