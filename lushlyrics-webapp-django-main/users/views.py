from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Import your RegistrationForm from the appropriate location
from .models import Account  # Import your Account model if not imported already

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            # Extract cleaned data from the form
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            
            # Create a new user instance and save it to the database
            user = Account.objects.create_user(
                email=email,
                username=username,
                password=password,
            )
            user.save()
            
            messages.success(request, 'Registration Successful')
            return redirect('register')  # Redirect to the login page or another appropriate URL after registration
    else:
        form = RegistrationForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'registration/signup.html', context)
