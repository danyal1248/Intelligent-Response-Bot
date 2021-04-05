from django import forms
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo,Job_Management,Question_Bank,Interview_Invite,Question_BankDetail



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
    attrs = {
    'class' : 'form-control',
    'id'    : 'email-login',
    'placeholder': 'User Name'

    }

    ))
    password = forms.CharField(widget=forms.PasswordInput(

    attrs = {
    'class' : 'form-control',
    'id'    : 'pwd-login',
    'placeholder': 'Password'

    }

    ))
class InterviewerForm(forms.Form):
    Invitation_Code = forms.CharField(widget=forms.TextInput(
    attrs = {
    'class' : 'form-control',
    'id'    : 'pwd-login',
    'placeholder': 'Enter Your Code To Access Your Interview'

    }

    ))
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'form-control','id' : 'pwd-login','placeholder': 'Enter Your Password','autocomplete':'off'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Enter Your User Name','autocomplete':'off'}),
            'email': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Email','autocomplete':'off'}),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('site_portfolio','profile_picture')
        widgets = {
                'site_portfolio': forms.TextInput(attrs={'class' : 'form-control',
                'id'    : 'pwd-login','placeholder': 'Enter Website URL','autocomplete':'off'}),
                'profile_picture': forms.TextInput(attrs={'class' : 'form-control',
                'id'    : 'pwd-login','placeholder': 'Email','autocomplete':'off','type':"file"}),
            }



class Job_ManagementForm(forms.ModelForm):
    CHOICEStwo = (
        (0,'Select Your Department'),
        ('digital', 'digital'),
        ('HR', 'HR'),
        ('creative', 'creative'),
        ('Sales', 'Sales'),
        ('Accounts', 'Accounts'),
    )
    department = forms.ChoiceField(choices=CHOICEStwo,widget=forms.Select(attrs={'class' : 'form-control',
    'id'    : 'pwd-login','placeholder': 'Select Question Domain'}))
    class Meta():
        model = Job_Management
        fields = ('job_title','job_type','experience','department','expiry_date')
        widgets ={
            'job_title': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Job Title'}),
            'job_type': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Job Type'}),
            'experience': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Previous Experience in Years'}),
            'department': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Department'}),
            'expiry_date': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Expire Date', 'type' : 'date'}),
            }


class Question_BankForm(forms.ModelForm):
    CHOICES = (
        (0,'Select Question Type'),
        ('Introductory', 'Introductory'),
        ('Aptitude', 'Aptitude'),
    )
    CHOICEStwo = (
        (0,'Select Your Department'),
        ('digital', 'digital'),
        ('HR', 'HR'),
        ('creative', 'creative'),
        ('Sales', 'Sales'),
        ('Accounts', 'Accounts'),
        )
    Question_Domain = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class' : 'form-control',
    'id'    : 'pwd-login','placeholder': 'Select Question Domain'}))

    Department = forms.ChoiceField(choices=CHOICEStwo,widget=forms.Select(attrs={'class' : 'form-control',
    'id'    : 'pwd-login','placeholder': 'Select Question Domain'}))
    class Meta():
        model = Question_Bank
        fields = ('Department','Question_Domain','question','correct_answer','choice_two','choice_three','choice_four')
        widgets ={
            'question': forms.Textarea(attrs={'class' : 'form-control',
            'id'    : 'pwd-textarea','placeholder': 'Write Question that you have to ask'}),
            'correct_answer': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Enter Correct Option'}),
            'choice_two': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Enter Second Option'}),
            'choice_three': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Enter Third Option'}),
            'choice_four': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Enter Four Option'}),
            }



class Question_Bank_Detail_Form(forms.ModelForm):
    CHOICES = (
        (0,'What type of question'),
        ('Introductory', 'Introductory'),
        ('Aptitude', 'Aptitude'),
    )
    CHOICEStwo = (
        (0,'Select Your Department'),
        ('digital', 'digital'),
        ('HR', 'HR'),
        ('creative', 'creative'),
        ('Sales', 'Sales'),
        ('Accounts', 'Accounts'),
    )
    Question_Domain_Detail = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class' : 'form-control',
    'id'    : 'pwd-login','placeholder': 'Select Question Domain'}))
    Department = forms.ChoiceField(choices=CHOICEStwo,widget=forms.Select(attrs={'class' : 'form-control',
    'id'    : 'pwd-login','placeholder': 'Select Question Domain'}))

    class Meta():
        model = Question_BankDetail
        fields = ('Department','Question_Domain_Detail','question')
        widgets ={
            'question': forms.Textarea(attrs={'class' : 'form-control',
            'id'    : 'pwd-textarea','placeholder': 'Write Question that you have to ask'}),
                }



class Interview_InviteForm(forms.ModelForm):

    class Meta():
        model = Interview_Invite
        fields = ('jobtitle','Interviewr_name','Interview_Email','Interviewr_Resume','Interviewr_Experience','Interview_expiry_date','Interviewr_Contact_Number','Interviewr_Last_Company','Interviewr_Country','Interview_Profile')
        widgets ={
            'Interviewr_name': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Candidate Name'}),

            'Interview_Email': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Candidate Email'}),

            'Interviewr_Experience': forms.Textarea(attrs={'class' : 'form-control',
            'id'    : 'pwd-textarea','placeholder': 'Relevant Experience'}),

            'Interview_expiry_date': forms.DateInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Interview Expiry date','type':'date'}),

            'Interviewr_Contact_Number': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Candidate Contact Number'}),

            'Interviewr_Last_Company': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Last Company'}),

            'Interviewr_Country': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Country Name'}),


            'Interview_Profile': forms.TextInput(attrs={'class' : 'form-control',
            'id'    : 'pwd-login','placeholder': 'Enter Linkdin Profile'}),

            }
