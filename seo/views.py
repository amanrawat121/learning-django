from django.shortcuts import render

# Create your views here.
def seohome(request):
    return render(request, "seo/home.html")