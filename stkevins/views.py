from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
class KevinsPageView(TemplateView):
    template_name = 'stkevins/stkevins_home.html'