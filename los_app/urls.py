"""sarcipilot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from los_app.apis.karza.pan_verification.views_pan_verification import PANAuthentication
# from los_app.apis.karza.bank_verification.views_bank_verification import BankVerificationAPI
from django.urls import path
from los_app.apis.cashfree.aadhar_ocr.views_aadhaar_ocr import AadhaarOcr
from los_app.apis.cashfree.bank_verification.views_bank_verification import BankVerification



urlpatterns = [
    # Karza apis
    # path('pan_authentication/', PANAuthentication.as_view(), name='karza_pan_authentication'),
    # path('karza_bank_verification/', BankVerificationAPI.as_view(), name='karza_bank_verification'),

    # Cashfree apis 
    path('aadhaar_ocr_verification/', AadhaarOcr.as_view(), name='aadhaar_ocr_verification'),
    path('bank_verification/', BankVerification.as_view(), name='bank_verification'),

]
