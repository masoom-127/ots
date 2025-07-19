from django.shortcuts import render
from django.template import loader # Import loader to load templates on web pages on  browser
from django.http import HttpResponse,HttpResponseRedirect # Import HttpResponse to send response to browser
from django.urls import reverse # Import reverse to redirect to a different URL
from OTS.models import *

def welcome(request):
    templates = loader.get_template('welcome.html')
    return HttpResponse(templates.render())
# def candidateRegistrationForm(request):
#     templates = loader.get_template('registration_form.html')
#     return HttpResponse(templates.render())
def candidateRegistration(request):
    pass
def loginView(request):
    pass
def candidateHome(request):
    pass
def testpaper(request):
     pass
def calculateTestResult(request):
    pass
def testResultHistory(request):
    pass
def showTestresult(request):
    pass
def logoutView(request):
    pass
