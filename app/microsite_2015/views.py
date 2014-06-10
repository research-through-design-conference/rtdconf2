from django.shortcuts import render, get_object_or_404
from microsite_2015.models import Page

# Create your views here.
def home(request):
        page = get_object_or_404(Page, title='Home')
        # now return the rendered template
        return render(request, 'microsite_2015/home.html', {'page': page})

def about(request):
        page = get_object_or_404(Page, title='What is the Research Through Design Conference?')
        # now return the rendered template
        return render(request, 'microsite_2015/about.html', {'page': page})

def attending(request):
        page = get_object_or_404(Page, title='Attending')
        # now return the rendered template
        return render(request, 'microsite_2015/attending.html', {'page': page})

def organisers(request):
        page = get_object_or_404(Page, title='Organisation')
        # now return the rendered template
        return render(request, 'microsite_2015/organisers.html', {'page': page})
