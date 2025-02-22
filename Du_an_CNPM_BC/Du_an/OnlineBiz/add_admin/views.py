from django.shortcuts import render

def index(request):
    return render(request, 'add_admin/index.html')


