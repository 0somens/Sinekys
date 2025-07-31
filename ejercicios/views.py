from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext as _


# Prueba de diagnóstico
class DiagnosticTestView(View):
    def get(self, request):
        return render(request, "diagnostico/index.html")
