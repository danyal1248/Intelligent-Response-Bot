from django.urls import path
from first_app import views

app_name = 'first_app'



urlpatterns = [
path('form/',views.form_view,name='form_view'),
path('webhook/',views.webhook,name='webhook'),
path('ranking/',views.ranking,name='ranking'),
path('Interview_Invitation/',views.interview_invitation,name='interview_invite'),
path('Interview_Invitation/<user>',views.interview_invitation,name='interview_invite'),
path('job_management/',views.job_management,name='job_management'),
path('job_management/<user>',views.job_management,name='job_management'),
path('Question-bank-landing/',views.Question_bank_landing,name='Question_bank_landing'),
path('Question_bank/',views.Question_bank,name='Question_bank'),
path('Question_bank/<user>',views.Question_bank,name='Question_bank'),
path('Question_bank_Detail/',views.question_Detail,name='Question_bank_Detail'),
path('Question_bank_Detail/<user>',views.question_Detail,name='Question_bank_Detail'),
path('registration/',views.register,name='register'),
path('login/', views.user_login,name='user_login'),
path('Interview/', views.Interview_login,name='Interviewer_login'),
path('answer/',views.answers,name='interview_answer'),
path('detail_answer/',views.detailanswers,name='detail_answer'),
path('rankingreport/',views.rankingreport,name='rankingreport'),
path('Interview_landing/',views.interviewlanding,name='Interview_landing')


]
