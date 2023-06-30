from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeMOdelAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','city' , 'pin', 'states','mobile' , 'email','job_city','profile_image','my_file']
