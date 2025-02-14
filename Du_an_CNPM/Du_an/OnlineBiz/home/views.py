from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from add_admin.models import Product
from add_admin.models import Client
from add_admin.models import Order



# Create your views here.

def home (request):
    return render(request, 'page.html')

def add_product (request ):
    product, created = Product.objects.get_or_create(
    id=1, 
    defaults={
        "tensanpham": "Sản phẩm mẫu",
        "dongia": 0  # Hoặc giá trị mặc định khác
        }
    )
    template = loader.get_template('home/product/product-add.html')
    context = {
        'products': product,
    }
    return HttpResponse(template.render(context, request))  

def product_list(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    return render(request, 'home/product/products.html', {'products': products})

def add_client(request):
    client, created = Client.objects.get_or_create(
        id=1,
        defaults={
            'hoten': 'Khách hàng mẫu',
            'gioitinh': 'Khác',
            'email': 'sample@example.com',
            'ngaysinh': None,
            'trangthai': True
        }
    )
    
    template = loader.get_template('home/account/client-add.html')
    context = {
        'client': client,
    }
    return HttpResponse(template.render(context, request))

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'home/account/clients.html', {'clients': clients})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'home/product/orders.html', {'orders': orders})


