
from django.contrib import admin
from django.urls import path, include
from products.views import home
import accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= 'home'),
    path('account/', include('accounts.urls')),
]


