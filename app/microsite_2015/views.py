from django.shortcuts import render

# Create your views here.
def home(request):
        # now return the rendered template
        return render(request, 'microsite_2015/home.html')

def about(request):
        # now return the rendered template
        return render(request, 'microsite_2015/about.html')

def attending(request):
        # now return the rendered template
        return render(request, 'microsite_2015/attending.html')

def organisation(request):
        # now return the rendered template
        return render(request, 'microsite_2015/organisation.html')
