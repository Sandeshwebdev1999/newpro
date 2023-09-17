"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name = 'base'),
    path('', views.index, name = 'index'),
    
    path('product/<slug:slug>', views.product_detail, name = 'product_detail'),
    path('product/', views.product, name = 'product'),
    path('product/filter-data',views.filter_data,name="filter-data"),

    path('404', views.error_404, name = '404'),
    path('account/my_account', views.my_account, name = 'my_account'),
    path('profile/my_profile', views.my_profile, name = 'my_profile'),
    path('profile/my_profile/update', views.profile_update, name = 'profile_update'),
    # path('profile/search/', views.search, name = 'search'),
    path('search/', views.search, name = 'search'),
    path('main/about', views.about, name = 'about'),
    path('main/my_order', views.my_order, name = 'my_order'),
    path('main/contact', views.contact, name = 'contact'),
    path('main/userask', views.userask, name = 'userask'),
    path('main/whishlist', views.whishlist, name = 'whishlist'),
    # (r'^/wishlist/', include('wishlist.urls')),
    path('main/privacy', views.privacy, name = 'privacy'),
    path('mobiles/', views.mobiles, name = 'mobiles'),
    path('watches/', views.watches, name = 'watches'),
    path('sarees/', views.sarees, name = 'sarees'),

    path('main/department1/<slug:slug>', views.department1_detail, name = 'department1_detail'),
    path('department', views.department, name = 'department'),
    path('main/department1', views.department1, name = 'department1'),
    # path('main/department2', views.department2, name = 'department2'),
    # path('main/department3', views.department3, name = 'department3'),
    # path('main/department4', views.department4, name = 'department4'),


    path('account/register', views.register, name = 'handleregister'),
    path('account/login', views.login, name = 'handlelogin'),
    
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('cart/checkout/',views.checkout,name='checkout'),
    path('cart/placeorder/',views.placeorder,name='placeorder'),
    path('cart/thank_you/',views.thank_you,name='thank_you'),
    

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
