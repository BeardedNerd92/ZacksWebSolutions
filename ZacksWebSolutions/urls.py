from django.contrib import admin
from django.urls import path

from core.views import index
from core.views import about
from core.views import contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
