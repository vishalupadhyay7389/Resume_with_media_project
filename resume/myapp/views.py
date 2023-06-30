from django.shortcuts import render
from .forms import ResumeForms
from .models import Resume
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self , request):
        form = ResumeForms()
        candidates = Resume.objects.all()
        return render(request , 'myapp/home.html' , {'candidates':candidates , 'form':form})
    def post(self,request):
        form = ResumeForms(request.POST , request.FILES)
        if form.is_valid():
         form.save()
         return render(request , 'myapp/home.html' , {'form':form})
class CandidateView(View):
    def get(self,request,pk):
        candidate = Resume.objects.get(pk = pk)
        return render(request , 'myapp/candidate.html',{'candidate':candidate})


