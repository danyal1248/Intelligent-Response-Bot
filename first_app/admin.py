from django.contrib import admin
from first_app.models import newtable,UserProfileInfo,Job_Management,Question_Bank,Interview_Invite,Question_BankDetail,Question_Detail_Answer,codecheck

# Register your models here.
admin.site.register(newtable)
admin.site.register(UserProfileInfo)
admin.site.register(Job_Management)
admin.site.register(Question_Bank)
admin.site.register(Interview_Invite)
admin.site.register(Question_BankDetail)
admin.site.register(Question_Detail_Answer)
admin.site.register(codecheck)
