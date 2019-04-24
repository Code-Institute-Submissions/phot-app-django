from django.shortcuts import render
from users.models import CustomUser, Pictures
from django.db.models import Count




def leaderboard(request):
    return render(request, 'rank/rank.html')