from django.shortcuts import render
from .forms import WaitlistForm
from .models import User
from django.http import JsonResponse

def join_waitlist(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            referral_code = form.cleaned_data.get('referral_code')
            new_user = form.save(commit=False)

            # Handle referral code logic
            if referral_code:
                try:
                    referrer = User.objects.get(referral_code=referral_code)
                    referrer.referrals_count += 1
                    referrer.save()
                except User.DoesNotExist:
                    pass  # Ignore invalid referral codes

            # Save the new user
            new_user.save()
            return render(request, 'thank_you.html', {'referral_code': new_user.referral_code})
    else:
        form = WaitlistForm()

    return render(request, 'waitlist.html', {'form': form})

def leaderboard(request):
    top_referrers = User.objects.order_by('-referrals_count')[:10]  
    data = list(top_referrers.values('name', 'referrals_count'))
    return JsonResponse(data, safe=False)