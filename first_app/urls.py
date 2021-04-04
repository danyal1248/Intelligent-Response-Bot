from django.urls import path
from first_app import views


app_name = 'first_app'

urlpatterns = [

path('help/',views.help,name='help'),
path('login/',views.user_login,name='user_login'),
path('form/',views.form_view,name='form_view'),
path('webhook/',views.webhook,name='webhook'),
path('ranking/',views.ranking,name='ranking'),
path('Interview_Invitation/',views.interview_invitation,name='interview_invite'),
path('job_management/',views.job_management,name='job_management'),
path('Question_bank/',views.Question_bank,name='questionbank'),
path('registration/',views.register,name='register'),
]
