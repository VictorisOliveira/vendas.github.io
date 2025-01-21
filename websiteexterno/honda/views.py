from django.shortcuts import render

def home(request):
    return render(request, 'site.html')

# Create your views here.
