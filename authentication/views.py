from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)

            # redirect(to) will return to the URL given 
            return redirect("home")
        
        # If either the account/password is invalid, it will render the following error message.
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, "login.html", {"error_message" : error_message})
            
        
    # render(request, template_name)
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            # Redirect to the home page after successful registration
            return redirect('home')
        # Invalid information
        else:
            pass
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, "home.html")