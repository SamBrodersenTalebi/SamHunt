from django.contrib import admin
from django.urls import path
#import view from product app
from product import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #render home page from product app
    path('', views.home, name="home"),
    path('accounts/', include('account.urls')),
    path('products/', include('product.urls')),
]
