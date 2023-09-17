from django.shortcuts import redirect, render, get_object_or_404
from app4.models import slider, banner_area, Main_Category, Product, Category,Color,Brand, Coupon_Code,Sub_Category,Order,Contact,OrderItem,special_offer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min , Sum
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
#from .forms import WishlistItemForm





def base(request):
    return render(request, 'main/base2.html')


def index(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]
    product = Product.objects.all()
    sub_category = Sub_Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID)
    else:
        product = Product.objects.all()


    main_category = Main_Category.objects.all()
    product = Product.objects.filter(section__name = "Top Deal Of The Day")
    context = {
        'sliders' : sliders,
        'banners' : banners,
        'main_category' : main_category,
        'product' : product,
    }
    return render(request, 'main/index.html' ,context)

def product_detail(request,slug):
    category = Category.objects.all()
    offer = special_offer.objects.all().order_by('-id')[0:]
    product = Product.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    sub_category = Sub_Category.objects.all()
    BrandID = request.GET.get('brandID')
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif BrandID:
        product = Product.objects.filter(brandID=BrandID).order_by('-id')
    else:
        product = Product.objects.all()

    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    ColorId = request.GET.get('colorId')
    sub_categoryID = request.GET.get('sub_category')

    
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)

    elif ColorId:
        product = Product.objects.filter(color=ColorId)
    elif sub_categoryID:
        product = Product.objects.filter(sub_category = sub_categoryID)
    else:
        product = Product.objects.all()

    context = {
        'category' : category,
        'product' : product,
        'min_price' : min_price,
        'max_price' : max_price,
        'FilterPrice' : FilterPrice,
        'color' : color,
        'brand': brand,
        'sub_category': sub_category,
        'offer' : offer,
    }

    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect('404')

    context = {
        'product' : product,
    }


    return render(request, 'product/product_detail.html',context)


def department1_detail(request,slug):
    # category = Category.objects.all()
    product = Product.objects.all()
    main_category = Main_Category.objects.all()

    categoryID = request.GET.get('main_category')
    if categoryID:
        product = Product.objects.filter(main_category = categoryID)
    else:
        product = Product.objects.all()


    context = {
        'main_category' : main_category,
        'product' : product,
    }


    return render(request, 'main/department_detail.html',context)




def error_404(request):
    return render(request, 'product/error.html')


def my_account(request):
    return render(request, 'account/my_account.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already exists')
            return redirect('login')


        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email-Id is already exists')
            return redirect('login')
       

        user = User(
            username = username,
            email = email,
            
        )
        user.set_password(password)
        user.save()
        return redirect('login')
       
    # return render(request, 'account/my_account.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        if user is not None:

            auth_login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Email Or password are invalid')
            return redirect('login')


@login_required(login_url='/accounts/login/') 
def my_profile(request):
    return render(request, 'profile/my_profile.html')

def search(request):
    offer = special_offer.objects.all().order_by('-id')[0:]
    Query = request.GET.get('query')
    product = Product.objects.filter(product_name__icontains = Query)

    if not product:
        return render(request, 'product/error.html')

    context = {
        'product' : product,
        'offer' : offer,
    }
    return render(request, 'search.html',context)


    
def profile_update(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id = user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request, 'Profile are successfully Updated')
        return redirect(my_profile)

    # return redirect(my_profile)
  
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        

        contact = Contact(name=name, address=address)
        contact.save()
        return redirect('index')

    return render(request, 'main/contact.html')

def userask(request):
    return render(request, 'main/userask.html')

def whishlist(request):
    return render(request, 'main/whishlist.html')

def privacy(request):

    return render(request, 'main/privacy.html')



def product(request):
    category = Category.objects.all()
    offer = special_offer.objects.all().order_by('-id')[0:]
    product = Product.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    sub_category = Sub_Category.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    ColorId = request.GET.get('colorId')
    sub_categoryID = request.GET.get('sub_category')

    
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)
    elif ColorId:
        product = Product.objects.filter(color=ColorId)
    elif categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    elif sub_categoryID:
        product = Product.objects.filter(sub_category = sub_categoryID)
    else:
        product = Product.objects.all()



    context = {
        'category' : category,
        'product' : product,
        'min_price' : min_price,
        'max_price' : max_price,
        'FilterPrice' : FilterPrice,
        'color' : color,
        'brand': brand,
        'sub_category': sub_category,
        'offer' : offer,
    }
    
    return render(request, 'product/product.html',context)


def filter_data(request):
    categories = Category.objects.all()
    offer = special_offer.objects.all().order_by('-id')[0:]
    product = Product.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    sub_categories = Sub_Category.objects.all()
    BrandID = request.GET.get('brandID')
    categoryID = request.GET.get('category')
    sub_categoryID = request.GET.get('subcategory')
    if categoryID:
         product = Product.filter(subcategory__category__name=categoryID)
    if sub_categoryID:
        product = Product.filter(subcategory__name=sub_categoryID)
    if categoryID:
        product = Product.objects.filter(category=categoryID).order_by('-id')
    elif BrandID:
        product = Product.objects.filter(brandID=BrandID).order_by('-id')
    else:
        product = Product.objects.all()
    

    context = {
        # 'category' : category,
        'product' : product,
        # 'min_price' : min_price,
        # 'max_price' : max_price,
        # 'FilterPrice' : FilterPrice,
        'color' : color,
        'brand': brand,
        # 'sub_category': sub_category,
        'offer' : offer,
    }
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    product = Product.objects.all()
    return render(request, 'product/product.html',context)



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    cart = request.session.get('cart')
    packing_cost = sum(i['packing_cost'] for i in cart.values() if i)
    tax = sum(i['tax'] for i in cart.values() if i)

    coupon_code = Coupon_Code.objects.all()
    valid_coupon = None
    coupon = None
    invalid_coupon = None
    if request.method == 'GET':
        coupon_code = request.GET.get('coupon_code')
        if coupon_code:
            try:
                coupon = Coupon_Code.objects.get(code=coupon_code)
                valid_coupon = "Applicable on it"
            except:
                invalid_coupon = "Not Applicable"


    context ={
        'packing_cost' : packing_cost,
        'tax' : tax,
        'coupon' : coupon,
        'valid_coupon' : valid_coupon,
        'invalid_coupon' : invalid_coupon,
    }
    return render(request, 'cart/cart.html',context)

    


def checkout(request):
    # if request.method == "POST":
    #     uid = request.session.get('_auth_user_id')
    #     user = User.objects.get(id=uid)
    #     state = request.POST.get('state')
    #     firstname = request.POST.get('firstname')
    #     lastname = request.POST.get('lastname')
    #     address = request.POST.get('address')
    #     city = request.POST.get('city')
    #     postcode = request.POST.get('postcode')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     amount = request.POST.get('amount')

    #     order = Order(
    #         state = state,
    #         firstname = firstname,
    #         address = address,
    #         city = city,
    #         postcode = postcode,
    #         email = email,
    #         phone = phone,
    #         amount = amount,
    #     )
    #     order.save()
        # return redirect('index')
        
    # coupon_discount = None
    # if request.method == "POST":
    #     coupon_discount = request.POST.get('coupon_discount')

    # cart = request.session.get('cart')
    # packing_cost = sum(i['packing_cost'] for i in cart.values() if i)
    # tax = sum(i['tax'] for i in cart.values() if i)

    # tax_and_packing_cost = (packing_cost + tax)

    # context = {
    #     'tax_and_packing_cost' : tax_and_packing_cost,
    #     'coupon_discount' : coupon_discount,
    #     'product' : product,

    # }
    return render(request, 'cart/checkout.html')

def placeorder(request):
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id = uid)
        cart = request.session.get('cart')
        state = request.POST.get('state')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')

        order = Order(
            user = user,
            firstname = firstname,
            lastname = lastname,
            phone = phone,
            postcode = postcode,
            city = city,
            state = state,
            address = address,
            email = email,
            amount = amount,

        )
        order.save()
        
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b

            item = OrderItem(
                order = order,
                product = cart[i]['product_name'],
                image = cart[i]['feature_image'],
                Quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                total = total,    
            )
            item.save()
            messages.success(request, 'Order Successfully placed ! Keep Shopping.')
        
    return render(request, 'cart/placeorder.html') 


def department(request):
    Query = request.GET.get('cat')
    product = Product.objects.filter(product_name__icontains = Query)

    if not product:
        return render(request, 'product/error.html')

    context = {
        'product' : product,
    }
    return render(request, 'department.html',context) 

def department1(request):

    product = Product.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    sub_category = Sub_Category.objects.all()

    Query = request.GET.get('query')
    product = Product.objects.filter(product_name__icontains = Query)

    context = {
        'product' : product,
    }
    
  
    
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    ColorId = request.GET.get('colorId')

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:

        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)

    elif ColorId:
        product = Product.objects.filter(color=ColorId)
    else:
        product = Product.objects.all()

    context = {
        'product' : product,
        'min_price' : min_price,
        'max_price' : max_price,
        'FilterPrice' : FilterPrice,
        'color' : color,
        'sub_category' : sub_category,
    }


    return render(request, 'main/department1.html' ,context)


def department2(request):

    product = Product.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    ColorId = request.GET.get('colorId')

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:

        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)

    elif ColorId:
        product = Product.objects.filter(color=ColorId)
    else:
        product = Product.objects.all()

    context = {
        'product' : product,
        'min_price' : min_price,
        'max_price' : max_price,
        'FilterPrice' : FilterPrice,
        'color' : color,
    }


    return render(request, 'main/department2.html' ,context)


def department3(request):

    product = Product.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()

    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    ColorId = request.GET.get('colorId')

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:

        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)

    elif ColorId:
        product = Product.objects.filter(color=ColorId)
    else:
        product = Product.objects.all()

    context = {
        'product' : product,
        'min_price' : min_price,
        'max_price' : max_price,
        'FilterPrice' : FilterPrice,
        'color' : color,
    }


    return render(request, 'main/department3.html' ,context)



def department4(request):
    return render(request, 'main/department4.html')


def department1_detail(request,slug):
    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect('404')

    context = {
        'product' : product,
    }


    return render(request, 'product/product_detail.html',context)

def thank_you(request):
    return render(request, 'cart/thank_you.html')

def mobiles(request):
    # product = SmartPhone.objects.all().order_by('-id')[:]
    
    product = Product.objects.filter(section__name = "Mobiles")

    context = {
        'product' : product,  
    }
    return render(request, 'mobiles.html',context)


def watches(request):
    product = Product.objects.all().order_by('-id')


    context = {
        'product' : product,
    }
    return render(request, 'watches.html',context)


def sarees(request):
    product = Product.objects.all().order_by('-id')[:]

    context = {
        'product' : product,
    }
    return render(request, 'sarees.html',context)

def my_order(request):
    order = Order.objects.all()
    orderitem = OrderItem.objects.all()
    context = {
        'order' : order,
        'orderitem' : orderitem,

    }
    return render(request, 'main/my_order.html',context)
