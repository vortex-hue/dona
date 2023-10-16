from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView, FormView
from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .utils import make_xrp_payment  # Import your XRP payment function

from .models import CampaignModel, Donation
from .forms import DonationForm


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['campaigns'] = CampaignModel.objects.all()

        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class CampaignsView(ListView):
    model = CampaignModel
    template_name = 'campaigns.html'
    context_object_name = 'campaigns'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        campaign_id = self.kwargs.get('pk')

        if campaign_id:
            campaign = get_object_or_404(CampaignModel, pk=campaign_id)
            campaign_percentage = campaign.calculate_percentage()
            context['campaign_percentage'] = campaign_percentage

        return context
    

class CampaignDetailView(View):
    template_name = 'campaign-details.html'
    form_class = DonationForm

    def get(self, request, *args, **kwargs):
        campaign = get_object_or_404(CampaignModel, pk=kwargs['pk'])
        form = self.form_class()
        context = {
            'campaign': campaign,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        d_seed = request.POST.get('seed')  # Get the donor's seed or address
        xrp_amount = request.POST.get('xrp_amount')
        campaign = get_object_or_404(CampaignModel, pk=kwargs['pk'])
        form = self.form_class(request.POST)

        if form.is_valid():
            donor_name = form.cleaned_data['name']
            donor_email = form.cleaned_data['email']
            donor_seed = form.cleaned_data['seed']
            donation_amount = form.cleaned_data['amount']
            donor_message = form.cleaned_data['message']

            # Create and save the donation
            donation = Donation.objects.create(
                name=donor_name,
                email=donor_email,
                amount=donation_amount,
                seed="Not to saved",
                message=donor_message,
                campaign=campaign
            )

            if donor_seed and donation_amount and donor_name:
                # Perform XRP payment using WalletConnect
                xrp_amount = str(int(donation_amount))
                # print(type(d_seed), d_seed, type(xrp_amount), xrp_amount)
                # 'sEdVqhXpTQGEktU8j8bNYduiX2oUGbm', '12'
                # sEd7BsgBifEjESjj9KmpHK8hmZbJHje
                xrp_payment_successful = make_xrp_payment(d_seed, xrp_amount)

                if xrp_payment_successful:
                    # Payment was successful, update the donation record if needed
                    campaign.current_amount += donation_amount
                    donation.save()
                    return redirect("xrpl:thank_you_page")
                else:
                    # Payment failed, handle errors appropriately
                    print("XRP payment failed.")
                    return redirect("xrpl:payment_error_page")

        
            # Redirect to a thank you page or handle other payment methods here

        # If the form is not valid, re-render the form with errors
        context = {
            'campaign': campaign,
            'form': form,
        }
        return render(request, self.template_name, context)
    

class EventView(TemplateView):
    template_name = 'event.html'

class EventDetailView(TemplateView):
    template_name = 'event-details.html'

class ContactView(TemplateView):
    template_name = 'contact.html'


class ThankyouView(TemplateView):
    template_name = 'thankyou.html'

class ErrorView(TemplateView):
    template_name = 'error.html'