from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact-us.html')

def shopDetail(request):
    return render(request, 'shop-Detail.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def myAccount(request):
    return render(request, 'my-account.html')

def wishlist(request):
    return render(request, 'wishlist.html')