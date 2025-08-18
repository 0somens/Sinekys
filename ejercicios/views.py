from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Prueba de diagnóstico
@method_decorator(login_required, name='dispatch')
class DiagnosticTestView(View):
    
    def get(self, request):
        return render(request, "diagnostico/index.html")
