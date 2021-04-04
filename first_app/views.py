from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from first_app.models import newtable,UserProfileInfo
from . import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
import json


def index(request):
    return render(request,'firstapp/index.html')

def help(request):
    dynamic_Statment = {'check':'this is help.html'}
    return render(request,'firstapp/help.html',context=dynamic_Statment)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            if user.is_active:
                get_data = UserProfileInfo.objects.get(user = user)
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse("Account is not active yet")
        else:
            print("tried to login")
            return HttpResponse("Account is not active yet")
    else:
        form = forms.LoginForm()
        return render(request,'firstapp/login.html',{'form':form})

@login_required(login_url = '/login/')
def dashboard(request):
    dynamic_Statment = {'check':'this is help.html'}
    return render(request,'firstapp/dashboard.html',context=dynamic_Statment)

@login_required(login_url = '/login/')
def ranking(request):
    dynamic_Statment = {'check':'this is help.html'}
    return render(request,'firstapp/ranking.html',context=dynamic_Statment)

@login_required(login_url = '/login/')
def interview_invitation(request):
    dynamic_Statment = {'check':'this is help.html'}
    return render(request,'firstapp/interview_invite.html',context=dynamic_Statment)

@login_required(login_url = '/login/')
def job_management(request):
    dynamic_Statment = {'check':'this is help.html'}
    return render(request,'firstapp/job_management.html',context=dynamic_Statment)
@login_required
def Question_bank(request):
    dynamic_Statment = {'check':'this is help.html'}
    return render(request,'firstapp/Question_bank.html',context=dynamic_Statment)


def form_view(request):
        form = forms.LoginForm()
        return render(request,'firstapp/backendform.html',{'form':form})

def register(request):
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if "profile_picture" in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request,'firstapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})




@csrf_exempt
def webhook(request):
    # build a request object
    req = json.loads(request.body)
    # get action from json
    action = req.get('queryResult').get('action')
    print(req.get('queryResult'))
    # return a fulfillment message
    fulfillmentText = {'fulfillmentText': 'This is Django test response from webhook.'}
    # return response
    return JsonResponse(fulfillmentText, safe=False)


# Create your views here.
