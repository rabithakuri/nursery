from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("shop/", views.shop, name="shop"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact-us/", views.contact, name="contact-us"),
    path("shop-detail/", views.shopDetail, name="shop-detail"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("my-account/", views.myAccount, name="my-account"),
    path("wishlist/", views.wishlist, name="wishlist"),



]
