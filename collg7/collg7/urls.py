from django.contrib import admin
from django.urls import path
from poll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name='home'),
    # path('home/',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('page/',views.page,name='page'),
]
