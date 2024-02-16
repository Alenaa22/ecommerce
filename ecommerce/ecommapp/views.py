from django.shortcuts import render,redirect
from django.views import View
from ecommapp.forms import UserRegister,UserLoggin,CartForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from ecommapp.models import Products,Category,Carts,Orders
from django.core.mail import send_mail,settings



# Create your views here.
class Homeview(View):
    def get(self,request,*args,**kwargs):
        data=Products.objects.all()
        return render(request,'index.html',{'products':data})
    
class RegisterView(View):
    def get(self,request):
       form=UserRegister()
       return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserRegister(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'register.html')
            return HttpResponse('success')
        else:
            messages.error(request,'invaid')
            return redirect('home_view')
        
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=UserLoggin()
        return render(request,'log.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserLoggin()
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=uname,password=password)
        if user:
            login(request,user)
            messages.success(request,'login successful')
            return redirect('home_view')
        else:
            messages.error(request,'invalid credentials')
            return redirect('log_view')
        
class UserLogout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'logout successful')
        return redirect('home_view')
    
class ProductDetails(View):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get('id')
        product=Products.objects.get(id=pid)
        return render(request,'productdetails.html',{'product':product})
    
class AddToCartView(View):
    def get(self,request,*args,**kwargs):
        form=CartForm()
        id=kwargs.get('id')
        product=Products.objects.get(id=id)
        return render(request,'addtocart.html',{'form':form,'product':product})
    def post(self,request,*args,**kwargs):
        u=request.user
        pid=kwargs.get('id')
        p=Products.objects.get(id=pid)
        q=request.POST.get('quantity')
        Carts.objects.create(user=u,quantity=q,product=p)
        return redirect('home_view')

class CartListView(View):
    def get(self,request,*args,**kwargs):
        cart=Carts.objects.filter(user=request.user).exclude(status="order placed")
        return render(request,'cartlist.html',{'carts':cart})

class PlaceOrderView(View):
    def get(self,request,*args,**kwargs):
        form=OrderForm()
        return render(request,'placeorder.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        cart_id=kwargs.get('cart_id')
        cart=Carts.objects.get(id=cart_id)
        user=request.user
        address=request.POST.get('address')
        mail=request.POST.get('mail')
        Orders.objects.create(user=user,cart=cart,address=address,mail=mail)
        send_mail('confirmation','orderplaced successfuly',settings.EMAIL_HOST_USER,[mail])
        cart.status='order-placed'
        cart.save()
        return redirect('home_view')


class CartDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        data=Carts.objects.get(id=id)
        data.delete()
        return redirect('list_cart')
