from django.shortcuts import render

# Create your views here.
def home(request):
        # now return the rendered template
        return render(request, 'microsite_2015/home.html')
