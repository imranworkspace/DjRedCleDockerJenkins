from django.contrib import admin
from django.urls import path
from myapp.views import cel_view,home,viewall
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cel_view),
    path('home/', home,name='home'),
    path('all/',viewall,name='all'),
    path('all/<int:pk>/',viewall,name='all'),
]
