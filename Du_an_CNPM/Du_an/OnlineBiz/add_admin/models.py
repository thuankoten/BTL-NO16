from django.db import models

# Bảng loaitaikhoan
class Account_type(models.Model):
    tenloaitaikhoan = models.CharField(max_length=255)

    def __str__(self):
        return self.tenloaitaikhoan

# Bảng taikhoan
class Account(models.Model):
    tentruycap = models.CharField(max_length=255, unique=True)
    matkhau = models.CharField(max_length=255)
    maloaitaikhoan = models.ForeignKey(Account_type, on_delete=models.SET_NULL, null=True)
    hoten = models.CharField(max_length=255, blank=True, null=True)
    trangthai = models.BooleanField(default=True)

    def __str__(self):
        return self.tentruycap

# Bảng khachhang
class Client(models.Model):
    GIOI_TINH_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
        ('Khác', 'Khác'),
    ]
    
    hoten = models.CharField(max_length=255)
    gioitinh = models.CharField(max_length=10, choices=GIOI_TINH_CHOICES)
    email = models.EmailField(unique=True)
    ngaysinh = models.DateField(null=True, blank=True)
    trangthai = models.BooleanField(default=True)

    def __str__(self):
        return self.hoten

# Bảng donhang
class Order(models.Model):
    makhachhang = models.ForeignKey(Client, on_delete=models.CASCADE)
    ngaylap = models.DateTimeField(auto_now_add=True)
    tongtien = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Đơn hàng {self.id} - {self.makhachhang.hoten}"

# Bảng danhmucsanpham
class Product_catalog(models.Model):
    tendanhmuc = models.CharField(max_length=255)
    trangthai = models.BooleanField(default=True)

    def __str__(self):
        return self.tendanhmuc

# Bảng sanpham
class Product(models.Model):
    tensanpham = models.CharField(max_length=255)
    hinhanh = models.ImageField(upload_to='sanpham/', null=True, blank=True)
    madanhmuc = models.ForeignKey(Product_catalog, on_delete=models.SET_NULL, null=True)
    soluong = models.PositiveIntegerField(default=0)
    dongia = models.DecimalField(max_digits=10, decimal_places=2)
    trangthai = models.BooleanField(default=True)

    def __str__(self):
        return self.tensanpham

# Bảng chitietdonhang
class Order_details(models.Model):
    madonhang = models.ForeignKey(Order, on_delete=models.CASCADE)
    masanpham = models.ForeignKey(Product, on_delete=models.CASCADE)
    soluong = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.madonhang} - {self.masanpham.tensanpham}"