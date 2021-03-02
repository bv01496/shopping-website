from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.http import HttpResponse, JsonResponse
from .models import Tags
from home.forms import AddressForm
from django.contrib import messages
from .models import Products,Shopcart,Ordered,Address
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def catlist(request,pk):
    products = Products.objects.filter(tags = pk)       
    tags = Tags.objects.get(id = pk).name
    return render(request,'products/catagory_list.html',{"products":products,'tag':tags})

@ login_required
def add_cart(request):
    if request.method == 'POST':
        rprod = request.POST.get('product')
        inst = Shopcart.objects.get(id=rprod).delete()
        checkout = checkoutprice(request)
        return JsonResponse({'status':'sucess','checkout':checkout})
    else:
        prod = request.GET.get('product')
        product = Products.objects.get(id=prod)
        order_instance,created = Shopcart.objects.get_or_create(customer=request.user,product =product)
        return JsonResponse({'status': 'added to cart'})

def checkoutprice(request):
    instance = Shopcart.objects.filter(customer=request.user)
    checkout = 0
    for prod in instance:
        quant = prod.quantity
        checkout += int(prod.product.price)*quant 
    return checkout

@ login_required
def usercart(request):
    instance = Shopcart.objects.filter(customer= request.user)
    checkout = checkoutprice(request)
    return render (request,'products/user_cart.html',{'products':instance,'checkout':checkout})

class ProdDetail(DetailView):
    model = Products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p = self.kwargs['pk']
        catagories = Products.objects.get(pk=p).tags.all()
        same_catagory = []
        for catagory in catagories:
            products = Products.objects.filter(tags__name = catagory).exclude(pk=p)
            for product in products:
                if product not in same_catagory:
                    same_catagory.append(product)
        context["same_catagory"] = same_catagory
        return context
    

def alter_cart_prod(request):
    if request.method == 'POST':
        cartid = request.POST['dec_prod']
        cart = Shopcart.objects.get(id = cartid)
        if cart.quantity == 1:
            cart.delete()
            current_cart = 0
            return JsonResponse({'current_cart':current_cart,'checkout':checkoutprice(request)})
        else:
            cart.quantity -= 1
            cart.save()
            current_cart = cart.quantity
            return JsonResponse({'current_cart':current_cart,'checkout':checkoutprice(request)})

    else:
        cartid = request.GET['inc_prod']
        cart = Shopcart.objects.get(id = cartid)
        cart.quantity += 1
        cart.save()
        current_cart = cart.quantity
        return JsonResponse({'current_cart':current_cart,'checkout':checkoutprice(request)})

class Search(ListView):
    model = Products
    template_name = 'products/search.html'
    def get_queryset(self):
        query = self.request.GET.get('search')
        query_set = super().get_queryset()
        return query_set.filter(name__icontains = query).union(query_set.filter(tags__name__icontains = query))

def ordercheckout(request):
    if request.method == 'POST':
        total_products = Shopcart.objects.filter(customer= request.user)
        selected_address = Address.objects.get(id=request.POST.get('select_address'))
        for product in total_products:
            Ordered.objects.create(customer = product.customer, product= product.product,quantity=product.quantity,dilivery_address=selected_address)
            product.delete()
        messages.success(request,'your order been placed successfully')
        return redirect('/')
    else:
        orders = Shopcart.objects.filter(customer= request.user)
        checkout = checkoutprice(request)
        existing_address = Address.objects.filter(user=request.user)
        return render(request,'products/order.html',{'orders':orders,'totalprice':checkout,'existing_address':existing_address,'addressform':AddressForm()})

def add_address(request):
    if request.method == 'POST':
        user = request.user
        location = request.POST.get('location')
        street = request.POST.get('street')
        pincode = request.POST.get('pincode')
        phonenumber = request.POST.get('phonenumber')
        Address.objects.create(user=user,location=location,street=street,pincode=pincode,phonenumber=phonenumber)
    return redirect('placeorder')