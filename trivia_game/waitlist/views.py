from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm
from .models import User, LeaderboardEntry
from django.http import JsonResponse

def index(request):
    """View for the index/home page"""
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_welcome_email(user)
            request.session['user_id'] = user.id
            return redirect('welcome')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def welcome(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('signup')
    user = User.objects.get(id=user_id)
    return render(request, 'welcome.html', {'user': user})

def send_welcome_email(user):
    subject = 'Welcome to Chi.ke!'
    message = f'''Hi {user.first_name}!
    
Welcome to Chi.ke! Your referral code is: {user.referral_code}
# Share this link with friends: https://chi.ke/join/{user.referral_code}
Share this link with friends: https:///join/{user.referral_code}

Thanks for joining!
The Chi.ke Team'''

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )

def leaderboard_view(request):
    # Fetch leaderboard data sorted by referrals in descending order
    leaderboard = LeaderboardEntry.objects.all().order_by('-referrals')[:10]
    return render(request, 'template_name.html', {'leaderboard': leaderboard})

def api_leaderboard(request):
    leaderboard = LeaderboardEntry.objects.all().order_by('-referrals')[:10]
    data = [
        {'name': entry.name, 'image_url': entry.image_url, 'referrals': entry.referrals}
        for entry in leaderboard
    ]
    return JsonResponse(data, safe=False)
