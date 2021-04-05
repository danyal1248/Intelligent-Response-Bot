from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
# Create your models here.

class newtable(models.Model):
    user_id = models.CharField(max_length=256,blank=False)
    Code_id = models.CharField(max_length=100,blank = False)
    happy = models.CharField(max_length=100,blank = True)
    fear = models.CharField(max_length=100,blank = True)
    surprise = models.CharField(max_length=100,blank = True)
    sad = models.CharField(max_length=100,blank = True)
    neutral = models.CharField(max_length=100,blank = True)
    disgust = models.CharField(max_length=100,blank = True)
    angry = models.CharField(max_length=100,blank = True)
    profile_video = models.ImageField(blank = True, upload_to = 'profile_pics')
    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    site_portfolio =  models.URLField(blank = True)
    profile_picture = models.ImageField(blank = True, upload_to = 'profile_pics')

    def __str__(self):
        return self.user.username

class Job_Management(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    job_title = models.CharField(max_length=100,blank=True)
    job_type = models.CharField(max_length=100,blank=True)
    experience = models.CharField(max_length=100,blank=True)
    department = models.CharField(max_length=100,blank=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.job_title

class Question_Bank(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Department = models.CharField(max_length=100,blank=True)
    Question_Domain = models.CharField(max_length=100,blank=True)
    question = models.CharField(max_length=100,blank=True)
    correct_answer = models.CharField(max_length=100,blank = False)
    choice_two = models.CharField(max_length=100,blank = True)
    choice_three = models.CharField(max_length=100,blank = True)
    choice_four = models.CharField(max_length=100,blank = True)

    def __str__(self):
        return self.Question_Domain

class Question_BankDetail(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Department = models.CharField(max_length=100,blank=True)
    Question_Domain_Detail = models.CharField(max_length=100,blank=True)
    question = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.Question_Domain_Detail


def f():
    get_random = get_random_string(length=6)
    return get_random


class Interview_Invite(models.Model):
    jobtitle = models.CharField(max_length=100,blank = False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Invitation_Code = models.CharField(max_length=6,blank=False,unique=True,default=f)
    Interviewr_name = models.CharField(max_length=100,blank = True)
    Interview_Email = models.EmailField(max_length=100,blank = True)
    Interviewr_Resume = models.ImageField(blank=True,upload_to = 'user_cv')
    Interviewr_Experience = models.CharField(blank=True,max_length = 200)
    Interview_expiry_date = models.DateField(blank=True, null=True)
    Interviewr_Contact_Number = models.CharField(blank=False,max_length = 15)
    Interviewr_Last_Company = models.CharField(blank=True,max_length = 50)
    Interviewr_Country = models.CharField(blank=True,max_length = 50)
    Interview_Profile = models.URLField(blank=True,max_length = 100)

    def __str__(self):
        return self.Invitation_Code

class Question_Detail_Answer(models.Model):
    user_id = models.CharField(max_length=100,blank = False)
    Code_id = models.CharField(max_length=100,blank = False)
    Question_Name = models.CharField(max_length=100,blank = False)
    Answer_Name = models.CharField(max_length=500,blank=False)
    positive_Emotions = models.CharField(max_length=500,blank=True,null =True)
    Negative_Emotions = models.CharField(max_length=500,blank=True,null = True)
    Neutral_Emotions = models.CharField(max_length=500,blank=True,null = True)


    def __str__(self):
        return self.Question_Name
