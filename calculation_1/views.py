from django.shortcuts import render

def home(request):
    return render(request, 'calculation_2/home.html')
