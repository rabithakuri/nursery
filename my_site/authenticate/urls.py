from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('about/', views.about, name='about'),
    #path('cart/', views.cart, name='cart'),
   # path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('myaccount/', views.myaccount, name='myaccount'),
    #path('shop/', views.shop, name='shop'),
    path('shops/', views.shops, name='shops'),
    path('wishlist/', views.wishlist, name='wishlist'),
    
]

