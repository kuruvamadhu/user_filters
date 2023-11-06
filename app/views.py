from django.shortcuts import render

# Create your views here.
def usdf(request):
    d={'data':'hii madhu'}
    return render(request,usdf.html,d)
   