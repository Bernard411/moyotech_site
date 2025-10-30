from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('admissions/', admissions_view, name='admissions'),
    path('contact/', contact_view, name='contact'),
    path('courses/', courses_view, name='courses'),
    path('team/', team_view, name='team'),
    path('services/', services_view, name='services'),
    path('product/', product_view, name='product'),
]