from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from .models import Event, Sacrament, Society, Community, Parishioner, Levy, Contribution

# Create your views here.
class KevinsPageView(TemplateView):
    template_name = 'stkevins/stkevins_home.html'

class EventListView(ListView):
    queryset = Event.published.all()
    context_object_name = 'event_list'
    paginate_by = 4
    template_name = 'stkevins/event_list.html'

def event_detail(request, year, month, day, event):
    event = get_object_or_404(Event, slug=event,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    return render(request, 'stkevins/event_detail.html', {'event': event,})

class SacramentListView(ListView):
    model = Sacrament
    context_object_name = 'sacrament_list'
    template_name = 'stkevins/sacrament_list.html'

class SacramentDetailView(DetailView):
    model = Sacrament
    context_object_name = 'sacrament'
    template_name = 'stkevins/sacrament_detail.html'

    def get_object(self, queryset=None):
        return Sacrament.objects.get(slug=self.kwargs.get("slug"))

class SocietyListView(ListView):
    model = Society
    context_object_name = 'society_list'
    template_name = 'stkevins/society_list.html'

class SocietyDetailView(DetailView):
    model = Society
    context_object_name = 'society'
    template_name = 'stkevins/society_detail.html'

    def get_object(self, queryset=None):
        return Society.objects.get(slug=self.kwargs.get("slug"))

class CommunityListView(ListView):
    model = Community
    context_object_name = 'community_list'
    template_name = 'stkevins/community_list.html'

class CommunityDetailView(DetailView):
    model = Community
    context_object_name = 'community'
    template_name = 'stkevins/community_detail.html'

    def get_object(self, queryset=None):
        return Community.objects.get(slug=self.kwargs.get("slug"))

class LevyListView(ListView):
    model = Levy
    context_object_name = 'levy_list'
    template_name = 'stkevins/levy_list.html'

def levy_detail(request, year, month, day, levy):
    levy = get_object_or_404(Levy, slug=levy,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    return render(request, 'stkevins/levy_detail.html', {'levy': levy,})

class ContributionListView(ListView):
    model = Contribution
    context_object_name = 'contribution_list'
    template_name = 'stkevins/contribution_list.html'

def contribution_detail(request, year, month, day, contribution):
    contribution = get_object_or_404(Contribution, slug=contribution,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    return render(request, 'stkevins/contribution_detail.html', {'contribution': contribution,})

class ParishionerListView(ListView):
    model = Parishioner
    context_object_name = 'parishioner_list'
    template_name = 'stkevins/parishioner_list.html'

class ParishionerDetailView(DetailView):
    model = Parishioner
    context_object_name = 'parishioner'
    template_name = 'stkevins/parishioner_detail.html'

    def get_object(self, queryset=None):
        return Parishioner.objects.get(slug=self.kwargs.get("slug"))

class ContactPageView(TemplateView):
    template_name = 'stkevins/contact.html'

class HistoryPageView(TemplateView):
    template_name = 'stkevins/history.html'

class GalleryPageView(TemplateView):
    template_name = 'stkevins/gallery.html'

class SearchResultsView(ListView):
    model = Parishioner
    template_name = 'stkevins/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Parishioner.objects.filter(
            Q(name__icontains=query) | Q(id_number__icontains=query)
        )
        return object_list