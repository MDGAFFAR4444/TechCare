from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile, ContactMessage, Rating, Booking
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm


def index(request):
    return render(request, 'authentication/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        mobile = request.POST['mobile']
        error_message = None  # Initialize error_message as None

        if not username or not password or not confirm_password or not email or not mobile:
            error_message = "Please fill in all fields."
        elif password != confirm_password:
            error_message = "Passwords do not match."
        elif User.objects.filter(username=username).exists():
            error_message = "Username already exists."
        else:
            # Create User
            user = User.objects.create_user(
                username=username, password=password)
            # Create UserProfile and link it to the User
            user_profile = UserProfile.objects.create(
                user=user, email=email, mobile=mobile)
            # Redirect to the login page after successful registration
            return redirect('login')

        return render(request, 'authentication/register.html', {'error_message': error_message})

    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to your home page after successful login
            return redirect('home')
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'authentication/login.html', {'error_message': error_message})

    return render(request, 'authentication/login.html')


def home(request):
    return render(request, 'authentication/home.html')


def about(request):
    return render(request, 'authentication/about.html')


def contact(request):
    error_message = ""

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            error_message = "Please fill in all fields."
        else:
            # Create a new ContactMessage object and save it to the database
            contact_message = ContactMessage(
                name=name, email=email, message=message)
            contact_message.save()
            # Redirect to a thank you page or any other page you prefer
            return redirect('thank_you')

    return render(request, 'authentication/contact.html', {'error_message': error_message})


def thank_you(request):
    return render(request, 'authentication/thank_you.html')


def save_rating(request):
    if request.method == 'POST':
        # Assuming you have a hidden input field with name 'rating'
        rating_value = request.POST.get('rating')
        if rating_value is not None:
            Rating.objects.create(value=rating_value)
            return JsonResponse({'message': 'Rating saved successfully'})

    return JsonResponse({'message': 'Rating not saved'}, status=400)


def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a thank-you page or any other desired page
            return redirect('thank_you')  # Define a 'thank_you' URL pattern
    else:
        form = BookingForm()

    return render(request, 'booking/booking.html', {'form': form})
