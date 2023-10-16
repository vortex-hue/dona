from django.urls import path
from . import views


app_name = 'xrpl'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('campaign/', views.CampaignsView.as_view(), name='campaigns'),
    path('campaign-detail/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_details'),
    # path('events', views.EventView.as_view(), name='events'),
    # path('events-detail', views.EventDetailView.as_view(), name='event_details'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('thank-you', views.ThankyouView.as_view(), name='thank_you_page'),
    path('error', views.ErrorView.as_view(), name='payment_error_page'),
]
