from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICES = [
    ('Delhi','Delhi'),
    ('Patna','Patna'),
    ('Ranchi','Ranchi'),
    ('Dhanbad','Dhanbad'),
    ('Mumbai','Mumbai'),
    ('Kolkata','Kolkata'),
]

class ResumeForms(forms.ModelForm):
    gender = forms.ChoiceField(choices= GENDER_CHOICES , widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(label='Prefered job location' , choices= JOB_CITY_CHOICES , widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city' , 'pin', 'states','mobile' , 'email','job_city','profile_image','my_file']
        labels = {'name':'Full name' , 'dob':'Date of Birth','pin':'Pincode','email':'Email-Id','mobile':'Mobile no','profile_image':'Profile Images','my_file':'Document'}
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'states':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
