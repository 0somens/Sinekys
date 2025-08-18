from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'main_page.html')
    
    return render(request, 'index.html')


