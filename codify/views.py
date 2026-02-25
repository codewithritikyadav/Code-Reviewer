from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CodeReview
from .gemini import review_code

def home(request):
    return render(request, 'home.html')

@login_required(login_url="/login/")
def dashboard(request):
    ai_result = None

    if request.method == "POST":
        language = request.POST.get("language")
        code = request.POST.get("code")

        if language and code:
            ai_result = review_code(language, code)

    return render(request, "dashboard.html", {
        "ai_result": ai_result
    })



def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.first_name = full_name
        user.save()

        return redirect('login_page')

    return render(request, 'register.html')

def history(request):
    return render(request, 'history.html')
    
@login_required
def dashboard(request):
    ai_result = None

    if request.method == "POST":
        code = request.POST.get("code")
        language = request.POST.get("language")

        # Here you generate AI result (replace with your AI logic)
        ai_result =  review_code(code, language)  

        # Save to database
        CodeReview.objects.create(
            user=request.user,
            code=code,
            language=language,
            ai_result=ai_result
        )

    return render(request, "dashboard.html", {"ai_result": ai_result})
@login_required
def history(request):
    reviews = CodeReview.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "history.html", {"reviews": reviews})    

