from django.shortcuts import render, redirect
from django_hosts.resolvers import reverse
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'cathedral/home.html'

def inject_form(request):
    return {'form': ContactForm()}

def basecontactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Service Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'info@parishbits.com', ['okeyluvsu2004@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message Successfully Sent!')
            return redirect('cathedral:home')
        messages.warning(request, 'Error. Message was not sent!')
    return render(request, "_base.html", {'form': form})