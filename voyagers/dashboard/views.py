from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    # Render the HTML template index.html
    return render(request, 'dashboard.html')
def editing(request):
    return render(request, 'editing.html')
