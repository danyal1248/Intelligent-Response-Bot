from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from first_app.models import newtable,UserProfileInfo,Job_Management,newtable,Interview_Invite,Question_Bank,Question_BankDetail,Question_Detail_Answer,codecheck
from . import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
import json
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
import paralleldots
import base64
from django.core.files.base import ContentFile
from django.template import RequestContext
from django.utils.crypto import get_random_string

api_key   = "FKtFmXzzfCOjvOqj1wCq6qNDJGRHqBXdaJ3Ioh1xfls"
paralleldots.set_api_key( api_key )






def index(request):
    if request.method == "POST":
        return render(request,'firstapp/index.html',{"alert":"Record Submitted Succefully"})
    else:
        return render(request,'firstapp/index.html')

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

def Interview_login(request):
    if request.method == "POST":
        Invitation_Code_Data = request.POST.get('Invitation_Code')
        try:
            get_data = Interview_Invite.objects.get(Invitation_Code = Invitation_Code_Data)
            request.session['job_title'] = get_data.jobtitle
            request.session['job_user_fetch'] = get_data.user_id
            request.session['Invitation_code'] = get_data.Invitation_Code
            request.session['mcqs_filled'] = 'False'
            request.session['video_filled'] = 'False'
            request.session['details_filled'] = 'False'
            data_save = codecheck(Code_id = get_data)
            data_save.save()
            return HttpResponseRedirect(reverse('Interview_Exam'))
        except:
            form = forms.InterviewerForm()
            return render(request,'firstapp/interviewr_portal/interviewr_login.html',{'form':form,'message':'2Kindly Enter Correct Code or You already submit your Interview'})
    else:
        form = forms.InterviewerForm()
        return render(request,'firstapp/interviewr_portal/interviewr_login.html',{'form':form})

def interviewlanding(request):
    if request.method == "POST":
        if (request.session['mcqs_filled'] == 'True' and request.session['video_filled'] == 'True' and request.session['details_filled'] == 'True' ):
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'firstapp/interviewr_portal/Interview_landing.html',{'alert':"Complete Your Interview First"})
    else:
        return HttpResponse('Can,t Access this template Directly')



def Interview_Exam(request):
    try:
        job_user_fetch = request.session['job_user_fetch']
        filled = request.session['mcqs_filled']
        data = request.session['job_title']
        job_Data = Job_Management.objects.get(job_title = data,user_id=job_user_fetch)
        question_Data = job_Data.department
        quiz_data = Question_Bank.objects.filter(Department = question_Data )
        return render(request,'firstapp/interviewr_portal/Interview_exam.html',{'form':quiz_data,'mcqs_filled':filled})
    except:
        return HttpResponse('Can,t Access this template Directly')



def Interview_Detail_Exam(request):
    try:
        job_user_fetch = request.session['job_user_fetch']
        filled_detail = request.session['details_filled']
        data = request.session['job_title']
        job_Data = Job_Management.objects.get(job_title = data,user_id=job_user_fetch )
        question_Data = job_Data.department
        print(question_Data)
        quiz_data = Question_BankDetail.objects.filter(Department = question_Data )
        return render(request,'firstapp/interviewr_portal/Interview_exam_detail.html',{'form_detail':quiz_data,'detail_filled':filled_detail})
    except:
        return HttpResponse('Can,t Access this template Directly')



def video_recorder(request):
    try:
        if(request.method == "POST"):
            get_random_value = get_random_string(length=6)
            request.session['video_filled'] = "True"
            video_data = request.POST.get('image')
            format, imgstr = video_data.split(';base64,')
            ext = format.split('/')[-1]
            value = str(f'profile_pics/{get_random_value}.{ext}')
            video_data = ContentFile(base64.b64decode(imgstr), name=get_random_value+'.' + ext) # You can save this as file instance.
            user_code = request.session['Invitation_code']
            user_id = request.session['job_user_fetch']
            video = newtable(user_id=user_id,Code_id=user_code,profile_video=video_data)
            instance = video.save()
            data = newtable.objects.get(profile_video=value)
            happy = 0
            url = str(f"media/{data.profile_video}")
            try:
                happy=paralleldots.facial_emotion(url).get("facial_emotion")[0].get("score")
                fear=paralleldots.facial_emotion(url).get("facial_emotion")[1].get("score")
                surprise=paralleldots.facial_emotion(url).get("facial_emotion")[2].get("score")
                sad=paralleldots.facial_emotion(url).get("facial_emotion")[3].get("score")
                neutral=paralleldots.facial_emotion(url).get("facial_emotion")[4].get("score")
                disgust=paralleldots.facial_emotion(url).get("facial_emotion")[5].get("score")
                angry=paralleldots.facial_emotion(url).get("facial_emotion")[6].get("score")
                newtable.objects.update_or_create(profile_video=value,defaults={'happy': happy,'fear': fear,'surprise': surprise,'sad': sad,'neutral': neutral,'disgust': disgust,'angry': angry},)
                video_filled = 'True'
                return render(request,'firstapp/interviewr_portal/videorecorder.html',{'video_filled':video_filled})
            except:
                video_filled = 'True'
                newtable.objects.update_or_create(profile_video=value,defaults={'happy': 0,'fear': 0,'surprise': 0,'sad': 0,'neutral': 0,'disgust': 0,'angry': 0},)
                return render(request,'firstapp/interviewr_portal/videorecorder.html',{'video_filled':video_filled})

        else:
            video_filled = request.session['video_filled']
            return render(request,'firstapp/interviewr_portal/videorecorder.html',{'video_filled':video_filled})
    except:
        return HttpResponse('Can,t Access this template Directly')



@login_required(login_url = '/login/')
def dashboard(request):
    user = request.user
    return render(request,'firstapp/dashboard.html',{'user':user})

@login_required(login_url = '/login/')
def ranking(request):
        data = Interview_Invite.objects.filter(user_id = request.user)
        return render(request,'firstapp/ranking.html',{"data":data})

@login_required(login_url = '/login/')
def rankingreport(request):
    if(request.method == "POST"):
        code_Value = request.POST.get('code')
        data = Interview_Invite.objects.filter(user_id = request.user)
        positive_Emotions = 0
        Negative_Emotions = 0
        Neutral_Emotions = 0
        happy = 0
        fear=0
        surprise=0
        sad=0
        neutral=0
        disgust=0
        angry=0
        data_answer_detail = Question_Detail_Answer.objects.filter(Code_id = code_Value)
        video_answer_detail = newtable.objects.filter(Code_id = code_Value)
        if (data_answer_detail):
            for row in data_answer_detail:
                positive_Emotions+=float(row.positive_Emotions)
                Negative_Emotions+=float(row.Negative_Emotions)
                Neutral_Emotions+=float(row.Neutral_Emotions)
            for row in video_answer_detail:
                happy+=float(row.happy)
                fear+=float(row.fear)
                surprise+=float(row.surprise)
                sad+=float(row.sad)
                neutral+=float(row.neutral)
                disgust+=float(row.disgust)
                angry+=float(row.angry)
            return render(request,'firstapp/rankingreport.html',{"positive_Emotions":positive_Emotions,"positive_Emotions":positive_Emotions,"Negative_Emotions":Negative_Emotions,"Neutral_Emotions":Neutral_Emotions,"happy":happy,"fear":fear,"surprise":surprise,"sad":sad,"neutral":neutral,"disgust":disgust,"angry":angry,"ver":"True"})
        else:
            return render(request,'firstapp/rankingreport.html',{"ver":"False"})


@login_required(login_url = '/login/')
def interview_invitation(request,user=None):
    if(request.method == 'POST'):
        Interview_Invite_Form = forms.Interview_InviteForm(request.POST)
        if Interview_Invite_Form.is_valid():
            Interview_Invite_Form.jobtitle = request.POST['jobtitle']
            Interview_Invite_Form_instance = Interview_Invite_Form.save(commit=False)
            Interview_Invite_Form_instance.user_id = request.user
            Interview_Invite_Form_instance.save()
            try:
                data = Interview_Invite.objects.get(user_id=request.user,jobtitle=request.POST['jobtitle'],Interviewr_name=request.POST['Interviewr_name'],Interview_Email=request.POST['Interview_Email'])
                send_mail(
                str(f"Hello { data.Interviewr_name }"),
                str(f'You are Invited For the Interview and your Interview code is { data.Invitation_Code }'),
                'danyal@spectrum-vmlyr.com',
                [str(f'{ data.Interview_Email }')],
                fail_silently=False,)
                return HttpResponseRedirect('interview_invitation')
            except:
                form = forms.Interview_InviteForm()
                job_title_data = Job_Management.objects.filter(user_id = request.user)
                invite_data = Interview_Invite.objects.filter(user_id = request.user)
                return render(request,'firstapp/interview_invite.html',{'form' : form,'job_title_data':job_title_data,'alert':"User already give his interview with this email address",'invite_data':invite_data})


        else:
            form = forms.Interview_InviteForm()
            job_title_data = Job_Management.objects.filter(user_id = request.user)
            invite_data = Interview_Invite.objects.filter(user_id = request.user)
            return render(request,'firstapp/interview_invite.html',{'form' : form,'job_title_data':job_title_data,'alert':"Form is not Submitted Please fill all the required Fields",'invite_data':invite_data})

    elif request.GET.get("method")=='invite':
        value = request.GET.get("job_delete")
        instance = Interview_Invite.objects.filter(user_id=request.user,detail_id=value)
        instance.delete()
        form = forms.Interview_InviteForm()
        job_title_data = Job_Management.objects.filter(user_id = request.user)
        invite_data = Interview_Invite.objects.filter(user_id = request.user)
        return render(request,'firstapp/interview_invite.html',{'form' : form,'job_title_data':job_title_data,'alert':"Record Deleted Successfully",'invite_data':invite_data})


    else:
        form = forms.Interview_InviteForm()
        job_title_data = Job_Management.objects.filter(user_id = request.user)
        invite_data = Interview_Invite.objects.filter(user_id = request.user)
        return render(request,'firstapp/interview_invite.html',{'form' : form,'job_title_data':job_title_data,'invite_data':invite_data})

@login_required(login_url = '/login/')
def job_management(request,user=None):
    if request.method == "POST":
        if request.POST['department'] != '0':
            job_form = forms.Job_ManagementForm(request.POST)
            if job_form.is_valid():
                job_form_instance = job_form.save(commit=False)
                job_form_instance.user_id = request.user
                job_form_instance.save()
                return HttpResponseRedirect('job_management')
        else:
            form = forms.Job_ManagementForm()
            job_data = Job_Management.objects.filter(user_id = request.user)
            return render(request,'firstapp/job_management.html',{'form':form,'job_data':job_data,'alert':"Kindly Fill Form Properly"})
    elif request.GET.get("method")=='job':
        value = request.GET.get("job_delete")
        instance = Job_Management.objects.filter(user_id=request.user,detail_id=value)
        instance.delete()
        form = forms.Job_ManagementForm()
        job_data = Job_Management.objects.filter(user_id = request.user)
        return render(request,'firstapp/job_management.html',{'form':form,'job_data':job_data})

    else:
        form = forms.Job_ManagementForm()
        job_data = Job_Management.objects.filter(user_id = request.user)
        return render(request,'firstapp/job_management.html',{'form':form,'job_data':job_data})

@login_required(login_url = '/login/')
def Question_bank_landing(request):
    if request.GET.get("method") == 'detail':
        value = request.GET.get("job_delete")
        instance = Question_BankDetail.objects.filter(user_id=request.user,detail_id=value)
        instance.delete()
        Question_Bank_data = Question_Bank.objects.filter(user_id = request.user)
        Question_Bank_Detail = Question_BankDetail.objects.filter(user_id = request.user)
        return render(request,'firstapp/question_landing.html',{'Question_Bank_data':Question_Bank_data,'Question_Bank_Detail':Question_Bank_Detail,"record":"Record Deleted Successfully"})
    elif request.GET.get("method") == 'mcq':
        value = request.GET.get("job_delete")
        instance = Question_Bank.objects.filter(user_id=request.user,detail_id=value)
        instance.delete()
        Question_Bank_data = Question_Bank.objects.filter(user_id = request.user)
        Question_Bank_Detail = Question_BankDetail.objects.filter(user_id = request.user)
        return render(request,'firstapp/question_landing.html',{'Question_Bank_data':Question_Bank_data,'Question_Bank_Detail':Question_Bank_Detail,"record":"Record Deleted Successfully"})

    else:
        Question_Bank_data = Question_Bank.objects.filter(user_id = request.user)
        Question_Bank_Detail = Question_BankDetail.objects.filter(user_id = request.user)
        return render(request,'firstapp/question_landing.html',{'Question_Bank_data':Question_Bank_data,'Question_Bank_Detail':Question_Bank_Detail})


@login_required(login_url = '/login/')
def Question_bank(request,user=None):
    if request.method == "POST":
        if request.POST['Department'] != '0':
            q_bank_form = forms.Question_BankForm(request.POST)
            if q_bank_form.is_valid():
                q_bank_form_instance = q_bank_form.save(commit=False)
                q_bank_form_instance.user_id = request.user
                q_bank_form_instance.save()
                return HttpResponseRedirect('Question_bank')
        else:
            form = forms.Question_BankForm()
            return render(request,'firstapp/Question_bank.html',{'form_question':form,'alert':"Fill Form Properly Your missed something"})

    else:
        form = forms.Question_BankForm()
        return render(request,'firstapp/Question_bank.html',{'form_question':form})

@login_required(login_url = '/login/')
def question_Detail(request,user=None):
    if request.method == "POST":
        if request.POST['Department'] != '0':
            Question_Bank_Detail_Form = forms.Question_Bank_Detail_Form(request.POST)
            if Question_Bank_Detail_Form.is_valid():
                get_random = get_random_string(length=6)
                Question_Bank_Detail_Form_instance = Question_Bank_Detail_Form.save(commit=False)
                Question_Bank_Detail_Form_instance.user_id = request.user
                Question_Bank_Detail_Form_instance.save()
                return HttpResponseRedirect('question_Detail')
        else:
            form = forms.Question_Bank_Detail_Form()
            return render(request,'firstapp/Question_Bank_Detail.html',{'form':form,'alert':"Fill Form Properly Your missed something"})
    else:
        form = forms.Question_Bank_Detail_Form()
        return render(request,'firstapp/Question_Bank_Detail.html',{'form':form})


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

def answers(request):
    question_Data = Question_Bank.objects.all()
    scoretotal = 0
    for questionvalue in question_Data:
        correct = questionvalue.correct_answer
        entered_answer = request.POST.get(questionvalue.question)
        if(entered_answer == correct):
            scoretotal+=1
    print(scoretotal)
    request.session['mcqs_score'] = scoretotal
    request.session['mcqs_filled'] = 'True'
    return HttpResponseRedirect(reverse('Interview_Exam'))

def detailanswers(request):
    question_Data = Question_BankDetail.objects.all()
    p_data = request.session['Invitation_code']
    get_data = Interview_Invite.objects.get(Invitation_Code = p_data)
    f = Question_Detail_Answer.objects.create()
    for questionvalue in question_Data:
        entered_answer = request.POST.get(questionvalue.question)
        if entered_answer != None:
            f.user_id = str(get_data.user_id)
            f.Code_id = get_data.Invitation_Code
            f.Question_Name = questionvalue.question
            f.Answer_Name = entered_answer
            f.positive_Emotions = paralleldots.sentiment(entered_answer).get("sentiment").get("positive")
            f.Negative_Emotions = paralleldots.sentiment(entered_answer).get("sentiment").get("negative")
            f.Neutral_Emotions = paralleldots.sentiment(entered_answer).get("sentiment").get("neutral")
            f.save()
            request.session['details_filled'] = 'True'
        else:
            return HttpResponseRedirect(reverse('Interview_Detail_Exam'))

    return HttpResponseRedirect(reverse('Interview_Detail_Exam'))



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
