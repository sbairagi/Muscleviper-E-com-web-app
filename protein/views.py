from django.shortcuts import render , HttpResponse,redirect
from .models import Brands,Brandimage,Contact,Order
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json



# Create your views here.
def index(request):

    tranding = "YES"
    category1 = "weight loss"
    category2 = "daily vitals"
    category3 = "mass gainers"
    trandings = Brands.objects.filter(tranding_product=tranding)
    category1 = Brands.objects.filter(product_category=category1)
    category2 = Brands.objects.filter(product_category=category2)
    category3 = Brands.objects.filter(product_category=category3)
    brandimage = Brandimage.objects.all()[:8]


    params = {
        'tranding' : trandings,
        'category1' : category1,
        'category2' : category2,
        'category3' : category3,
        'brandimage' : brandimage,
    }
    return render(request, "index.html", params)


def product_view(request,id):
    product = Brands.objects.filter(bsno=id).first()
    category = product.product_category
    recommended = Brands.objects.filter(product_category=category).order_by('?')[:8]
    
    params = {
        'product' : product,
        'recommended' : recommended
    }
    return render(request, "product_view.html", params)


def brands_product(request,brands):


    products = Brands.objects.filter(product_brand=brands)
    paginator = Paginator(products, 20) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params = {
        'page_obj': page_obj,
        'products' : page_obj.object_list,
    }
    return render(request, "brands_product.html", params)

def categorial_product(request,category):


    products = Brands.objects.filter(product_category=category)
    paginator = Paginator(products, 20) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params = {
        'page_obj': page_obj,
        'products' : page_obj.object_list,
    }
    return render(request, "categorial_product.html", params)
    
def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    if request.method=="POST":
        email = request.POST.get("email")
        message = request.POST.get("Message")
        contact = Contact(email=email,message=message)
        contact.save()
        messages.success(request, "your contact detail has been sent successfully")
        return render(request,"contactus.html")
    return render(request,"contactus.html")


def checkout(request):
    # thank = 'ThankYou For Ordering. your order sent successfully'
    if request.method=='POST':
        itemsJson = request.POST.get("itemsJson")
        amount = request.POST.get("amount")
        name = request.POST.get("name")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2", "Dont Have")
        email = request.POST.get("email")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zip_code")
        phone = request.POST.get("phone")
        orderdetail = Order(itemsJson=itemsJson,amount=amount,name=name,address1=address1,address2=address2,email=email,city=city,state=state,zip_code=zip_code,phone=phone)
        orderdetail.save()
        messages.success(request, "your order has been placed successfully")
        params = {
            'thank' : 'ThankYou For Ordering. your order has been placed successfully'
        }
        return render(request,"checkout.html",params)
    
    return render(request,"checkout.html")
    

def search(request):
    # allposts = Post.objects.all()
    query = request.GET.get('query')
    if len(query)>78:
        allproducts=Brands.objects.none()
    if len(query)<1:
        allproducts=Brands.objects.none()
    else:
        allproducttitle = Brands.objects.filter(product_title__icontains=query)
        allproductdesc = Brands.objects.filter(product_desc__icontains=query)
        allproducts = allproducttitle.union(allproductdesc)
    if allproducts.count() == 0:
        messages.warning(request, 'No Search Result Found. Please Refine Your Query.')

    params = {'allproducts': allproducts, 'query':query}
    return render(request,"search.html", params)


#Authentication APIs
def handelSignup(request):
    if request.method == 'POST':
        #get the post perameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        usernameInDatabase = User.objects.filter(username= username)
        #check for errorneous inputs
        if usernameInDatabase:
            messages.error(request, "this username is not available. Please use a unique username")
            return redirect('/')
        #username should be under 10 character
        if len(username) > 10:
            messages.error(request,"username must be 10 characters")
            return redirect('/')

        #username should be alphanumeric

        if not username.isalnum() :
            messages.error(request,"username should only contains laters and characters")
            return redirect('/')

        #password should match

        if pass1 != pass2 :
            messages.error(request,"password do not match")
            return redirect('/')


        #create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your icoder acount has been successfully created")
        return redirect('/')

    else:
        return HttpResponse('<br><br><br><br><br><br><h1 align="center">404 - Not Found</h1>')

def handelLogin(request):
    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']
    user = authenticate(username=loginusername, password=loginpassword)
    if user is not None:
        login(request, user)
        messages.success(request,"successfully logedd in")
        return redirect('/')
    else:
        messages.error(request,"invalid credential, please try again. ")
        return redirect('/')

    return HttpResponse('<br><br><br><br><br><br><h1 align="center">404 - Not Found</h1>')

def handelLogout(request):
    logout(request)
    messages.success(request,"successfully logedd out")
    return redirect('/')