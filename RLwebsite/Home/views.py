from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import  Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def product(request):
    return render(request, 'Products.html')

def service(request):
    return render(request, 'Services.html')

def outcome(request):
    return render(request, 'Outcomes.html')

def innovation(request):
    return render(request, 'innovation.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'karry' and password == '2310':
            request.session['responses'] = {}
            return redirect('raslo')  
        else:
            context={'message':"The username or password you entered is incorrect."}
            return render(request, 'Login.html',context)
    return render(request, 'Login.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'Products.html', {'products': products})

def add_to_cart(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        image = request.POST.get("image")
        if product_name and price and image:
            price = float(price) 
            cart_items = request.session.get('cart_items', [])
            existing_item = next((item for item in cart_items if item['product_name'] == product_name), None)
            if existing_item:
                existing_item['quantity'] += 1 
            else:
                cart_items.append({
                    'product_name': product_name,
                    'price': price,
                    'image': image,
                    'quantity': 1,
                })
            request.session['cart_items'] = cart_items
            return redirect('cart') 
    return JsonResponse({"error": "Invalid request"}, status=400)

def cart(request):
    cart_items = request.session.get('cart_items', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def update_cart(request, product_name):
    action = request.POST.get('action')
    cart_items = request.session.get('cart_items', [])
    item = next((item for item in cart_items if item['product_name'] == product_name), None)
    if item:
        if action == 'increase':
            item['quantity'] += 1  
        elif action == 'decrease' and item['quantity'] > 1:
            item['quantity'] -= 1 
        request.session['cart_items'] = cart_items
    return redirect('cart')  

def remove_from_cart(request, product_name):
    cart_items = request.session.get('cart_items', [])
    cart_items = [item for item in cart_items if item['product_name'] != product_name]
    request.session['cart_items'] = cart_items
    return redirect('cart') 

@login_required
def checkout(request):
    cart_items = request.session.get('cart_items', [])  # Retrieve from session
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)  # Calculate total price

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

@login_required
def complete_checkout(request):
    cart.objects.filter(user=request.user).delete()
    return redirect('order_success') 

@login_required
def order_success(request):
    return render(request, 'order_success.html')

