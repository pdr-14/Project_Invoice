from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    return HttpResponse("Hello Word")
def dashboard(request):
    customer=150
    sales=200
    products=100
    return render(request,'dashboard.html',{'customer':customer, 'sales':sales, 'products':products})
@require_http_methods(["GET", "POST"])
def addproduct(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        piece=request.POST.get('pieces_in_packets', 0)
        if(piece == ''):
            piece = 0
        Product.objects.create(
             name=name,
             hsn=request.POST.get('hsn'),
             gst=request.POST.get('gst'),
             price=request.POST.get('price'),
             stock=request.POST.get('stock'),
             unit=request.POST.get('unit'),
             pieces_in_packets=float(request.POST.get('stock'))*float(piece)  # Default to 0 if not provided 
         )
        product_details = Product.objects.all()
        cardview=render_to_string('addproduct/productcard.html', {'productlist': product_details})
        return JsonResponse({"status": "success", "message": f"Product {name} added successfully!","html": cardview})
        
    else:
        product_details=Product.objects.all()
        return render(request,'addproduct.html',{"productlist":product_details})
@require_http_methods(["GET", "POST"])
def deleteproduct(request):
    if request.method == 'POST':
        product_id = request.POST.get('name')
        try:
            product = Product.objects.get(name=product_id)
            product.delete()
            product_details=Product.objects.all()
            cardview=render_to_string('addproduct/productcard.html', {'productlist': product_details})
             # Render the updated product list
             # Return a success message and the updated HTML
             # You can customize the response as needed
             # For example, you might want to return a success message or redirect to another page
             # Here, we are returning a JSON response with the updated HTML
            return JsonResponse({"status": "success", "message": f"Product {product_id} deleted successfully!", "html":cardview})
        except Product.DoesNotExist:
            product_details = Product.objects.all()
            cardview = render_to_string('addproduct/productcard.html', {'productlist': product_details})
            return JsonResponse({"status": "error", "message": "Product not found.", "html": cardview})
    else:
        product_details=Product.objects.all()
        return render(request,'addproduct.html',{"productlist":product_details})