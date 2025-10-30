from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def admissions_view(request):
    return render(request, 'admissions.html')

def courses_view(request):
    return render(request, 'courses.html')

def contact_view(request):
    return render(request, 'contact.html')


def team_view(request):
    return render(request, 'team.html')

def services_view(request):
    return render(request, 'service.html')

def product_view(request):
    return render(request, 'product.html')