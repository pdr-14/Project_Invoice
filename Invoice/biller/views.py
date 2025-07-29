from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Product,productloggin
from django.template.loader import render_to_string
import datetime


# Create your views here.
def login(request):
    return render(request,"login.html")
def home(request):
    return HttpResponse("Hello Word")
@login_required
def dashboard(request):
    customer=150
    sales=200
    products=100         
    return render(request,'dashboard.html',{'css/bootstrap.min.css" rel="stylesheet" integrity=ustomer':customer, 'sales':sales, 'products':products})
@require_http_methods(["GET", "POST"])
def addproduct(request):
    if request.method == 'POST':
    
        name=request.POST.get('name')
        piece=request.POST.get('pieces_in_packets', 0)
        if(piece == ''):
            piece = 0
        #checking product is present or not
        if Product.objects.filter(name=name).exists():
            product_details = Product.objects.all()
            cardview=render_to_string('addproduct/productcard.html', {'productlist': product_details})
            return JsonResponse({"status": "error", "message": f"Given Product {name} already exists!","html": cardview})
        else:
            Product.objects.create(
                name=name,
                hsn=request.POST.get('hsn'),
                gst=request.POST.get('gst'),
                price=request.POST.get('price'),
                stock=request.POST.get('stock'),
                unit=request.POST.get('unit'),
                each_piece_in_packets=float(piece),
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
        product_id
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
@require_http_methods(["GET", "POST"])
def editproduct(request):
    if request.method=="GET":
        name=request.GET.get('name')
        if name==None:
            product_details=Product.objects.all()
            return render(request,'addproduct.html',{"productlist":product_details})
        else:
            product=Product.objects.get(name=name)
            product_details ={
            'name': product.name,
            'hsn': product.hsn,
            'gst': product.gst,
            'price': product.price,
            'stock': product.stock,
            'unit': product.unit,
            'each_piece_in_packets': product.each_piece_in_packets,
            'pieces_in_packets': product.pieces_in_packets
            }
        return JsonResponse({"status":"success","product":product_details})
    elif request.method=="POST":
        name=request.POST.get('name')
        if(Product.objects.filter(name=name).exists()):
            piece=request.POST.get('pieces_in_packets', 0)
            if(piece == ''):
                piece = 0
            product_update=Product.objects.get(name=name)
            product_update.name=name
            product_update.hsn=request.POST.get('hsn')
            product_update.gst=request.POST.get('gst')
            product_update.price=request.POST.get('price')
            product_update.stock=request.POST.get('stock')
            product_update.unit=request.POST.get('unit')
            product_update.each_piece_in_packets=float(piece)
            product_update.pieces_in_packets=float(request.POST.get('stock'))*float(piece)
            product_update.save()
            product_details=Product.objects.all()
            cardview=render_to_string('addproduct/productcard.html', {'productlist': product_details})
            return JsonResponse({"status":"success","message":f"Product {name} updated successfully","html":cardview})
        else:
            return JsonResponse({"status":"error","message":f"Product {name} is not found"})
    else:
        return JsonResponse({"status":"error","message":"Invalid request method."})

#for the searching the product
@require_http_methods(["GET", "POST"])
def searchproduct(request):
    if request.method=="GET":
        productname=request.GET.get('name')
        if productname == None:
            product_details = Product.objects.all()
            cardview = render_to_string('addproduct/productcard.html', {'productlist': product_details})
            return JsonResponse({"status": "error", "message": "Please enter a valid product name.",'productlist': product_details, "html": cardview})
        else:
            try:
                product=Product.objects.filter(name__icontains=productname)
                product_details = list(product.values())
                cardview = render_to_string('addproduct/productcard.html', {'productlist': product_details})
                return JsonResponse({"status": "success", 'productlist': product_details,"html": cardview})
            except Product.DoesNotExist:
                product_details = Product.objects.all()
                cardview = render_to_string('addproduct/productcard.html', {'productlist': product_details})
                return JsonResponse({"status": "error", "message": f"Product {productname} not found.",'productlist': product_details,"html":cardview})

#for the viewproduct
@require_http_methods(["GET"])
def viewproduct(request):
    if request.method=="GET":
        productname=request.GET.get('name')
        try:
            product=Product.objects.get(name__icontains=productname)
            if product  is not  None:
                unit=product.unit
                eachpiecesinpackets=product.each_piece_in_packets
                piecesinpackets=product.pieces_in_packets
                convertedtopackets=0
                stock=product.stock
                remainigpieces=0
                if(unit.lower()=="packets"):
                    convertedtopackets=piecesinpackets/eachpiecesinpackets
                    splitedpackage=str(convertedtopackets).split(".")
                    stock=splitedpackage[0]
                    if int(stock)>=0:
                        remainigpieces= int(splitedpackage[1])*eachpiecesinpackets
                product_details ={
                'name': product.name,
                'hsn': product.hsn,
                'gst': product.gst,
                'price': product.price,
                'stock': stock,
                'unit': unit,
                'each_piece_in_packets': eachpiecesinpackets,
                'pieces_in_packets': piecesinpackets,
                 'remaing':remainigpieces
                }
                return JsonResponse({"status": "success", 'productlist': product_details})
            else:
                product_details = Product.objects.all()
                cardview = render_to_string('addproduct/productcard.html', {'productlist': product_details})
                return JsonResponse({"status": "error", "message": f"Product {productname} not found.",'productlist': product_details,"html":cardview})
        except Product.DoesNotExist:
                    product_details = Product.objects.all()
                    cardview = render_to_string('addproduct/productcard.html', {'productlist': product_details})
                    return JsonResponse({"status": "error", "message": f"Product {productname} not found.",'productlist': product_details,"html":cardview})
#for the customer to add
@require_http_methods(["GET","POST"])
def addcustomer(request):
    return render(request,"addcustomer.html")