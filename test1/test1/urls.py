from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('stuview/',views.Stu_views,basename='stuview'),
router.register('proview/',views.Product_view,basename='product'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
