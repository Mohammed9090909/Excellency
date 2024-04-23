from django.http import HttpRequest
from django.shortcuts import render
from main.models import Contactus


def index_view(request: HttpRequest):
   return render(request, "main/index.html")


def contactus_view(request: HttpRequest):
   msg = None
   try:
      if request.method == "POST":
         Contactus.objects.create(full_name=request.POST.get('full_name'),
                                  email=request.POST.get('email'),
                                  subject=request.POST.get('subject'),
                                  message=request.POST.get('message'),
                                  )
         msg = "تم ارسال رسالتك بنجاح"
   except Exception as e:
      pass
   return render(request, "main/contactus.html", {'msg': msg})


def lawyers_view(request: HttpRequest):
   return render(request, "main/lawyers.html")
