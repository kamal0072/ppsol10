from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('show/',views.show,name='show'),
    path('page/',views.page,name='page'),
    path('site/',views.site,name='site'),
]
