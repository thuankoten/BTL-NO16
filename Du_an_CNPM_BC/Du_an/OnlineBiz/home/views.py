from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from add_admin.models import Product
from add_admin.models import Client
from add_admin.models import Order
from django.contrib import messages
from add_admin.models import User
from django.contrib.auth import get_user_model
from add_admin.models import CustomUser
from django.contrib.auth.models import Group  

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

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):  # Kiểm tra mật khẩu
                request.session['user_id'] = user.id  # Lưu session
                messages.success(request, "Đăng nhập thành công!")
                return redirect('home')  # Chuyển đến trang chính
            else:
                messages.error(request, "Sai mật khẩu!")
        except User.DoesNotExist:
            messages.error(request, "Tài khoản không tồn tại!")

    return render(request, 'home/account/login.html')
CustomUser = get_user_model()  # Lấy model User (Django hoặc Custom)

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Mật khẩu không khớp.")
            return redirect("register.html")  # Sửa lại đúng name của URL

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại.")
            return redirect("register.html")

        # Kiểm tra email đã tồn tại chưa (nếu cần)
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email đã được sử dụng.")
            return redirect("register.html")

        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            user.is_staff = True
            user.save()

            # Thêm user vào group "Người Dùng"
            group, created = Group.objects.get_or_create(name="Người Dùng")  
            user.groups.add(group)

            messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")
            return redirect("login.html")  # Sửa lại đúng name của URL login
        except Exception as e:
            messages.error(request, f"Lỗi trong quá trình đăng ký: {e}")
            return redirect("register.html")

    return render(request, "home/account/register.html")