from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Import your RegistrationForm from the appropriate location
from .models import Account  # Import your Account model if not imported already

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            # Extract cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            
            # Create a new user instance and save it to the database
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.phone_number = phone_number
            user.save()
            
            messages.success(request, 'Registration Successful')
            return redirect('register')  # Redirect to the login page or another appropriate URL after registration
    else:
        form = RegistrationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'registration/signup.html', context)
