from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect ,HttpResponse
#from django.http import HttpResponse
from . models import Activities ,Excursions , Admin , Images ,Cart,CartProduct ,HotelAdmin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView ,ListView , FormView , TemplateView , View , CreateView
from django.contrib.auth import authenticate , login , logout 
from .forms import  CreateUserForm ,ActiviteForm , AdminLoginForm  ,ActiviteForm ,ExcursiosForm ,HotilLoginForm , Chekoutform
from django.contrib import messages
from .filters import ActivitiesFiter , ExcursiontFilter

import folium

from django.views import generic 
from django.urls import reverse_lazy
# Create your views here.
######################  Home viws page home hadi

#############################################################

class ChpingMixin(object):
    def dispatch(self,request,*args,**kwargs):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            if request.user.is_authenticated or request.user.hoteladmin:
                cart_obj.costomer = request.user.hoteladmin
                cart_obj.costemer2 = request.user 
                cart_obj.save()     
        return super().dispatch(request,*args, **kwargs)        




#######################################################


def Home(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') 
            messages.success(request , 'Account was created for' + user)
            return render(request , 'home.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username,password=password)

        if user is not None:
           login(request , user)
           return render(request,'home.html')
        else:
         errors = messages.info(request, 'Username OR passworde incorrect')
         return HttpResponse('<h3>Username OR passworde incorrect</h3>')         
    context = {
        'form':form ,
            
    }
    return render(request, 'home.html' , context)
def LogoutUser(request):
    logout(request)
    return redirect('myapp:home')

    
# Vweis Traget     
def excursions(request):
    excursions_menu_list = Excursions.objects.all()
    title_contains_qurey = request.GET.get('address_E')
    #address_contains_qurey = request.GET.get('price_contains')
    #print(address_contains)

    if title_contains_qurey != '' and title_contains_qurey is not None:
        excursions_menu_list = excursions_menu_list.filter(address_E=title_contains_qurey)

    m = folium.Map()
    m = m._repr_html_()  
    context = {
         'excursions_menu_list':excursions_menu_list ,
         'm':m,   

    }
    return render(request ,'excursions.html' , context  )
###### detail excoursion
def  ExDetail(request , slug): 
    excursions_detail = Excursions.objects.filter(slug=slug)
    context = {'detail':excursions_detail} 
    return render(request ,'excursionsdetail.html',context  )

# Add the Cart
class AddToCartView(TemplateView): 
    template_name = "addtocart.html"

    def get_context_data(self, **kwargs):
        # get product Id form request url 
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['pro_id']
        print(product_id , '**************')
        # get produtc 
        product_obj = Excursions.objects.get(id=product_id)


        # check if cart exixts 
        cart_id = self.request.session.get("cart_id", None)
        if cart_id: 
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart= cart_obj.cartproduct_set.filter(produt=product_obj)
            # iteme alredy exists in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.price_E
                cartproduct.save()
                cart_obj.total += product_obj.price_E
                cart_obj.save()
            # new itme is added in cart    
            else:
                cartproduct = CartProduct.objects.create(cart=cart_obj , produt=product_obj, rate=product_obj.price_E, quantity=1 , subtotal=product_obj.price_E)
                cart_obj.total += product_obj.price_E
                cart_obj.save()    
            print("old Cart")
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id']=cart_obj.id
            cartproduct = CartProduct.objects.create(cart=cart_obj , produt=product_obj, rate=product_obj.price_E, quantity=1 , subtotal=product_obj.price_E)
            cart_obj.total += product_obj.price_E
            cart_obj.save()
            print("new cart")    
        return context

# Mycart craet page 
class MyCartView(TemplateView):
    template_name = 'mycart.html'
    def get_context_data(self , **kwargs):
        context=super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id")
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart        
        return context 
# manage cart msah o zid f les produit 
class MangeCartView(View):
    def get(self , request , *args , **kwargs):
        print("This is manage cart")
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart 
        print(cp_id, action)
        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
            
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()
        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()          
        else:
            pass
        return redirect('myapp:mycart')
class EmptyCartView(View):
    def get(self , request, *args, **kwargs):
        cart_id = request.session.get("cart_id" , None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect('myapp:mycart')            


class ChechoutView(CreateView):
    template_name = "checkout.html"
    form_class = Chekoutform
    success_url = reverse_lazy('myapp:home')


    def dispatch(self , request , *args, **kwargs):
        if request.user.is_authenticated or request.user.hoteladmin:
            print('login user')
        else:
            return HttpResponse('<h1>ples login </h1>')    
        #print('halow horded if thse mthed dispatch')
        return super().dispatch(request, *args , **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context['cart'] = cart_obj
        return context
    def form_valid(self , form):
        cart_id = self.request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.discount = 0
            form.instance.total = cart_obj.total
            form.instance.order_status = "Order Received"

        else:
            return redirect('myapp:home')
        return super().form_valid(form)             
    pass



    
    








def Three(request):
    activites_menu_list = Activities.objects.all()
    title_contains_qurey = request.GET.get('address')
    #address_contains_qurey = request.GET.get('price_contains')
    #print(address_contains)

    if title_contains_qurey != '' and title_contains_qurey is not None:
        activites_menu_list = activites_menu_list.filter(address=title_contains_qurey)

    m = folium.Map()
    m = m._repr_html_()

    context = {
         'activites_menu_lists':activites_menu_list , 
         'm':m  

    }
    return render(request ,'Activitie.html' , context  ) 
############## hadi bach kay3aamar l form d activiti
def activitisform(request):
    if request.method =='POST':
        myform = ActiviteForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
    return render(request, 'adminpage/activitiesform.html' , {'myform':ActiviteForm} )
############## hadi bach kay3aamar l form d excourseion
def  Excursionsform(request):
    if request.method =='POST':
        myform = ExcursiosForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
    return render(request, 'adminpage/excursionsform.html' , {'myform':ExcursiosForm} )

############## hadi bach kaydkhño les admin ligay3amro o activiti ecoursin    
class  AdminLoginView(FormView):
    template_name = "adminpage/adminlogin.html"
    form_class = AdminLoginForm 
    success_url = reverse_lazy("myapp:pageadmin")
##### activiti viewise 
    def form_valid(self, form):   
            usernsme_a = form.cleaned_data.get('username')
            password_a = form.cleaned_data.get('password')
            data = authenticate(username=usernsme_a, password=password_a)
            if data is not None and Admin.objects.filter(user=data).exists():
                login(self.request , data)
            else:
                return render(self.request , self.template_name , {"form":self.form_class,"error":"Invalid credentials"})
            return super().form_valid(form)
############### hadi hadi pagehom les admin ligay3amro o activiti ecoursin main page 
class  HomePageView(TemplateView):
    template_name = "adminpage/mainpage.html"


################# Hotil page ###################3
class  HotilLoginForm(FormView):
    template_name = "adminpage/hotillogin.html"
    form_class =  HotilLoginForm
    success_url = reverse_lazy("myapp:pagehotiladmin")
##### activiti viewise 
    def form_valid(self, form):   
            usernsme_a = form.cleaned_data.get('username')
            password_a = form.cleaned_data.get('password')
            data = authenticate(username=usernsme_a, password=password_a)
            if data is not None and HotelAdmin.objects.filter(user=data).exists():
                login(self.request , data)
            else:
                return render(self.request , self.template_name , {"form":self.form_class,"error":"Invalid credentials"})
            return super().form_valid(form)
############### hadi hadi pagehom les admin ligay3amro o activiti ecoursin main page 
class  HomePageHotilView(TemplateView):
    template_name = "adminpage/pagehotiladmin.html"    
