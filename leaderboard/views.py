from django.shortcuts import render
from users.models import CustomUser, Pictures
from django.db.models import Count, Q, Sum
from django.contrib.auth.models import User


def leaderboard(request):
    leaderboard = Pictures.objects.all().values('user__full_name', 'user__profile_picture').annotate(amount_of_views=Sum('views')).order_by('-amount_of_views')[0:30]
    return render(request, 'leaderboard/leaderboard.html', {'leaderboard': leaderboard})