from django.shortcuts import render, redirect, get_object_or_404
from django_hosts.resolvers import reverse
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Reflection
from .forms import ContactForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'cathedral/home.html'

class TestPageView(TemplateView):
    template_name = 'cathedral/test_h.html'

class ReflectionListView(ListView):
    queryset = Reflection.published.all()
    context_object_name = 'reflection_list'
    paginate_by = 4
    template_name = 'cathedral/reflection_list.html'

def reflection_detail(request, year, month, day, reflection):
    reflection = get_object_or_404(Reflection, slug=reflection,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    return render(request, 'cathedral/reflection_detail.html', {'reflection': reflection,})

class ParishPageView(TemplateView):
    template_name = 'cathedral/parishes.html'

class GalleryPageView(TemplateView):
    template_name = 'cathedral/gallery.html'

class ContactPageView(TemplateView):
    template_name = 'cathedral/contact.html'

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
                send_mail(subject, message, 'info@parishbits.com', ['juddyblaise@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message Successfully Sent!')
            return redirect('cathedral:home')
        messages.warning(request, 'Error. Message was not sent!')
    return render(request, "_base.html", {'form': form})