from django.contrib import admin
from django.urls import path
from poll import views as poll_view
from enroll import views as enroll_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",poll_view.home,name='home'),
    path("enroll/",enroll_view.enroll_view,name='enroll'),
]
