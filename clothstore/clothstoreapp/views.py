from django.shortcuts import render,redirect
from clothstoreapp import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from clothstoreapp.models import Customer,User,cartentrties,Ladiesclothes,Mensclothes,Issue,Orderedd
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    # # Delete all data from User model
    # User.objects.all().delete()
    
    # # Delete all data from AnotherModel
    # Customer.objects.all().delete()
#     new_entry = Customer(
    
#     phon=0000000,
#     address='dubai'
# )

# # Save the instance to the database
#     new_entry.save()
#     print("saved")
    return render(request,'home.html')

@login_required(login_url='loginform')
def Sweetfruits(request):
    if request.method == 'POST':
        veg_id = request.POST.get('fruit_id')
        try:
            antic = get_object_or_404(Mensclothes, pk=veg_id)
            cart_entry = cartentrties.objects.create(
                user=request.user,
                men_cloth_cart=antic
            )
            cart_entry.save()
        except Exception as e:
            print("Error:", e)
            
    fruit=models.Mensclothes.objects.all()
    return render(request,'fruits.html',{"fruits":fruit})


# from django.urls import reverse
@login_required(login_url='loginform')
def vegetabalesfun(request):
    if request.method == 'POST':
        veg_id = request.POST.get('veg_id')
        try:
            ladies_cl = get_object_or_404(Ladiesclothes, pk=veg_id)
            cart_entry = cartentrties.objects.create(
                user=request.user,
                ladies_cloth_cart=ladies_cl
            )
            cart_entry.save()
        except Exception as e:
            print("Error:", e)
            
            
    llll=models.Ladiesclothes.objects.all()
    return render(request,'vegetables.html',{'vegetables':llll})

import time
from django.db import transaction
@login_required(login_url='loginform')
def Cart(request):
    if request.method == 'POST':
        messages.success(request, 'Your Clothes order has been shipped to your registered location.')
        user_entries = cartentrties.objects.filter(user=request.user)
        time.sleep(2)
    # Check if the user has any entries
        # if user_entries.exists():
        # # Delete the user's entries
        #     user_entries.delete()
        

        if user_entries.exists():
            # Start a transaction to ensure atomicity
            with transaction.atomic():
                # Iterate through each entry
                for entry in user_entries:
                    # Create a new entry in Orderedd
                    Orderedd.objects.create(
                        user=entry.user,
                        ladies_cloth_cart=entry.ladies_cloth_cart,
                        men_cloth_cart=entry.men_cloth_cart
                    )
                # Delete the user's entries from cartentrties
                user_entries.delete()        
    cart_entries = cartentrties.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_entries': cart_entries})

def help(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create a new instance of the Issue model
        new_issue = Issue(name=name, email=email, subject=subject, message=message)
        new_issue.save()
        messages.success(request, 'Your issue has been submitted successfully!')
    return render(request,'help.html')


def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['Address']
        password=request.POST['password']
        if User.objects.filter(email=email):
            messages.error(request,'⚠️ username already exists go for login')
            print('problem')
            return redirect('loginform')
        user = User.objects.create_user(username=email , email=email, first_name=name, last_name=lastname)
        user.set_password(password)
        fruitscustomer = Customer.objects.create(
            phon=phone,
            address=address
        )
        fruitscustomer.save()
        user.save()
        messages.success(request,'user has been succesfully created \n login now')
    return render(request,'register.html')



from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def login_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the provided email exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user is None:
            messages.error(request, "Username does not exist.")
            return redirect("loginform")

        # Authenticate the user
        user = authenticate(username=user.username, password=password)
        if user is not None:
            # Check if the user account is active
            if user.is_active:
                # Log the user in
                login(request,user)
                messages.success(request, 'Logged in successfully! Now you can go to your section.')
                # return redirect("cart")
                  # Redirect to dashboard or home page
            else:
                messages.error(request, 'Your account is disabled.')
        else:
            messages.error(request, 'Invalid password.')

    return render(request, 'loginform.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Customer
@login_required(login_url='loginform')
def updations_of_user(request):
    user_id = request.user
    try:
        customer_instance = Customer.objects.get(id=user_id.id)
        address = customer_instance.address
        phone_number = customer_instance.phon
        fisrtname=user_id.first_name
        emailid=user_id.email
        print(fisrtname,emailid,phone_number)
    except Customer.DoesNotExist:
        address = None
        phone_number = None
        print("error")
        # Consider a more informative error message here
    # updation work
        
# updating phone number
    if 'new-phone' in request.POST:
        new_phone = request.POST.get('new-phone')
        user = request.user
        try:
            customer = Customer.objects.get(id=user_id.id)
            customer.phon= int(new_phone)
            customer.save()
            messages.success(request, 'Phone number updated successfully.')
            return redirect('updation')

        except Customer.DoesNotExist:
            messages.error(request, 'Customer record not found.')

# updating address of user
    if 'new-address' in request.POST:
        new_address = request.POST.get('new-address')
        user = request.user
        try:
            customer = Customer.objects.get(id=user_id.id)
            customer.address= new_address
            customer.save()
            messages.success(request, 'Address updated successfully.')
            return redirect('updation')

        except Customer.DoesNotExist:
            messages.error(request, 'Customer record not found.')


    context = {'user_address': address, 'user_phone': phone_number,'user_name':fisrtname,'user_email':emailid}
    return render(request, 'updation.html',context)



@login_required(login_url='loginform')
def Ordered(request):
    # if request.method == 'POST':
        # messages.success(request, 'Your fruits and vegetables order has been shipped to your registered location.')
        # user_entries = cartentrties.objects.filter(user=request.user)
    # Check if the user has any entries
        # if user_entries.exists():
        # Delete the user's entries
            # user_entries.delete()


        # print("succied")
    cart_entries = Orderedd.objects.filter(user=request.user)
    return render(request, 'ordered.html', {'cart_entries': cart_entries})
