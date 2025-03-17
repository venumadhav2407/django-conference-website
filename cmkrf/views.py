from django.shortcuts import render, redirect
from .models import Country




# Create your views here.
def home(request):
    return render(request, "cmkrf/home.html")

def agenda(request):
    return render(request, "cmkrf/agenda.html")

def speakers(request):
    return render(request, "cmkrf/speaker.html")

def contact(request):
    return render(request, "cmkrf/contact.html")

def registration(request):
    return render(request, "cmkrf/registration.html")



def termsandcondition(request):
    return render(request, 'cmkrf/terms&condition.html')


# payment 
def payment(request):
    return render(request, "cmkrf/payment/payment.html")


def abstract(request):
    country = Country.objects.all()
    return render(request, 'cmkrf/abstractSubmit.html', {'country_name': country})

# import requests
# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.http import JsonResponse

# def verify_recaptcha(recaptcha_response):
#     secret_key = "YOUR_SECRET_KEY"
#     url = "https://www.google.com/recaptcha/api/siteverify"
#     data = {
#         'secret': secret_key,
#         'response': recaptcha_response
#     }
#     result = requests.post(url, data=data).json()
#     return result.get("success", False)

# def registration_view(request):
#     if request.method == "POST":
#         recaptcha_response = request.POST.get("g-recaptcha-response")
#         if not verify_recaptcha(recaptcha_response):
#             return JsonResponse({"error": "Invalid CAPTCHA. Please try again."}, status=400)

#         # Proceed with registration logic
#         return JsonResponse({"message": "Registration successful!"}, status=200)

#     return render(request, "registration_form.html")
