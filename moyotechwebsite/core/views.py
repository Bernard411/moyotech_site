from django.shortcuts import render

# Create your views here.
# your_app/views.py
from django.shortcuts import render
from .models import SoftwareProduct, Course, HostingPackage


def home_view(request):
    products = SoftwareProduct.objects.all()
    courses = Course.objects.all()
    hosting_packages = HostingPackage.objects.all()

    context = {
        'products': products,
        'courses': courses,
        'hosting_packages': hosting_packages,
    }
    return render(request, 'home.html', context)
def about_view(request):
    return render(request, 'about.html')

def admissions_view(request):
    return render(request, 'admissions.html')

def courses_view(request):
    return render(request, 'courses.html')

def contact_view(request):
    return render(request, 'contact.html')


# your_app/views.py
from django.shortcuts import render
from .models import TeamMember


def team_view(request):
    # Split the queryset into the two sections your template expects
    leadership = TeamMember.objects.filter(role_group='leadership')
    instructors = TeamMember.objects.filter(role_group='instructor')

    context = {
        'leadership': leadership,
        'instructors': instructors,
    }
    return render(request, 'team.html', context)

def services_view(request):
    return render(request, 'service.html')

# your_app/views.py
from django.shortcuts import render
from .models import Product

def product_view(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})