from django.shortcuts import render
from users.models import CustomUser, Pictures
from django.db.models import Count, Q, Sum
from django.contrib.auth.models import User


def leaderboard(request):
    user_and_views = Pictures.objects.values('user__full_name').annotate(amount_of_views=Sum('views')).order_by('-amount_of_views')
    return render(request, 'rank/rank.html', {'user_and_views': user_and_views})