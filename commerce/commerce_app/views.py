from django.shortcuts import render,redirect
from .models import Category,Product,Cart,Favourite
from  django.contrib import messages
from .forms import Customerform
from django.contrib.auth import login,authenticate,logout
import json
from django.http import JsonResponse

# Create your views here.
def home(request):
    product=Product.objects.all()
    return render(request,'index.html',{'product':product})
def register(request):
   form=Customerform()
   if request.method=='POST':
       form=Customerform(request.POST)
       if form.is_valid():
           form.save() 
           return redirect('login_page')
   return render(request,'register.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request,'logged in successfuly')
                    return redirect('home')
                else:
                    messages.error(request, "Your account is inactive.")
            else:
                messages.error(request, "Invalid username or password.")
        return render(request, 'login.html')
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successfully")
    return redirect('home')    
        
def collections(request):
    res=Category.objects.all()
    
    return render(request,'collections.html',{'res':res})
# def collectionsview(request,name):
#     if (Category.objects.filter(name=name)):
#         product=Product.objects.filter(category__name=name)
#         return render(request,'product.html',{"product":product,"category_name":name})
#     else:
#         messages.warning(request,"category not found in the page")
#         return redirect('collections')

# def productdetails(request,cname,pname):
#     if Category.objects.filter(name=cname):
#         if Category.objects.filter(name=pname):
#            product=Product.objects.filter(name=pname)  
#            return render(request,'productdetails.html',{"product":product})
#         else:
#             messages.error(request,"no such product here ") 
            # return redirect('collections')
    # else:
    #     messages.error(request,"no such product here ") 
    #     return redirect('collections')   
    # 
def collectionsview(request, name):
    if Category.objects.filter(name=name).exists():
        product = Product.objects.filter(category__name=name)
        return render(request, 'product.html', {"product": product, "category_name": name})
    else:
        messages.warning(request, "Category not found.")
        return redirect('collections')

def productdetails(request, cname, pname):
    if Category.objects.filter(name=cname).exists():
        product = Product.objects.filter(name=pname, category__name=cname).first()
        if product:
            return render(request, 'productdetails.html', {"product": product})
        else:
            messages.error(request, "No such product here.")
            return redirect('collections')
    else:
        messages.error(request, "Category not found.")
        return redirect('collections')  
       



def add_Cart(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'Please log in to add items to your cart'}, status=403)
        
        try:
            data = json.loads(request.body)
            product_qty = data.get('product_qty')
            product_id = data.get('pid')

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return JsonResponse({'status': 'Product not found'}, status=404)

            if Cart.objects.filter(user=request.user, product_id=product_id).exists():
                return JsonResponse({"status": "Product already in cart"}, status=200)
            
            if product.quantity >= product_qty:
                Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                return JsonResponse({"status": "Product added to cart"}, status=200)
            else:
                return JsonResponse({'status': 'Product stock not available'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'Invalid data'}, status=400)
        except Exception as e:
            return JsonResponse({'status': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)

def view_cart(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,'cart.html',{'cart':cart})
    else:
        return redirect("home")
def remove_cart(request,id):
    remove=Cart.objects.get(id=id)   
    remove.delete()
    return redirect('view_cart') 
def fav(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'Please log in to add items to your cart'}, status=403)
        
        try:
            data = json.loads(request.body)
            product_id = data.get('pid')
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return JsonResponse({'status': 'Product not found'}, status=404)
            if Favourite.objects.filter(user=request.user, product_id=product_id).exists():
                return JsonResponse({"status": "Product already in Favourite"}, status=200)
            Favourite.objects.create(user=request.user, product_id=product_id)
            return JsonResponse({'status':'add to favourite'},status=200)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'Invalid data'}, status=400)
        except Exception as e:
            return JsonResponse({'status': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)
def view_fav(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,'view_fav.html',{'fav':fav})
    else:
        return redirect("home")
def remove_fav(request,id):
    remove=Favourite.objects.get(id=id)   
    remove.delete()
    return redirect('view_fav')    
      

""" def add_Cart(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            try:
                data = json.loads(request.body)
                product_qty = data.get('product_qty')
                product_id = data.get('pid')
                
                product_status=Product.objects.get(id=product_id)
                if product_status:
                    if Cart.objects.filter(user=request.user.id,product_id=product_id):
                        return JsonResponse({"status":"product already in cart "},status=200)
                    else:
                        if product_status.quantity >= product_qty:
                            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                            return JsonResponse({"status":"product add to cart"},status=200)
                        else:
                            return JsonResponse({'status': 'Product stock not available'}, status=200)
            except json.JSONDecodeError:
                return JsonResponse({'status': 'Invalid data'}, status=400)
            except Exception as e:
                return JsonResponse({'status': str(e)}, status=500)
        else:
            return JsonResponse({'status': 'Please log in to add items to your cart'}, status=403)
    else:
        return JsonResponse({'status': 'Invalid request'}, status=400)
   
        
 """