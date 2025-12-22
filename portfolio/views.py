from django.shortcuts import render
from .models import Project

def portfolio_list(request):
    projects = Project.objects.all()
    return render(request, 'pages/portfolio.html', {'projects': projects})
