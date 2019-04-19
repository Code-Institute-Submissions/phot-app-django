from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView
import stripe 

stripe.api_key = settings.STRIPE_SECRET_KEY


class DonatePageView(TemplateView):
    template_name = 'donate/donate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
        

def charge_five(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'donate/charge_five.html')

def charge_ten(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'donate/charge_ten.html')
        
def charge_fifteen(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'donate/charge_fifteen.html')