from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path("agenda/", views.agenda, name="agenda"),
    path('speakers/', views.speakers, name='speakers'),
    path('contact/', views.contact, name='contact'),
    path('registration/', view=views.registration, name='registration'),
    path("api/payment", views.payment, name="payment"),
    path('terms&conditions/', views.termsandcondition, name='terms&conditions'),
    path('abstractSubmit/', views.abstract, name='abstract')
]