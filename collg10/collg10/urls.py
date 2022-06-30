from django.contrib import admin
from django.urls import path
from poll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/',views.home,name='home'),
    # path('home/home1',views.home,name='home'),
    # path('home/home1',views.home,name='home'),
    #--------------------------
    # path('home/<name>',views.home,name='home'),
    # path('home/home1/<str:python>',views.home,name='home'),
    path('home/<int:pk>',views.home,name='home'),
]
