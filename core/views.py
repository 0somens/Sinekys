from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def main_page(request):
    return render(request, 'main_page.html')


def about(request):
    return render(request, 'NoLogged/About.html')

def goals(request):
    return render(request, 'NoLogged/Goals.html')

def how_does_it_work(request):
    return render(request, 'NoLogged/HowDoesItWork.html')