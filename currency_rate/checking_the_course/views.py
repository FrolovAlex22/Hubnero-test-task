from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.core.cache import cache

from .models import СourseRequest



def get_current_rate(request):
    return HttpResponse('Все работает', status=200)