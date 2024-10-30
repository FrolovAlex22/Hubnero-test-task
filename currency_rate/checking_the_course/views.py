from datetime import datetime
import os

from dotenv import load_dotenv
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache

from .services import currency_rate

from .models import СourseRequest


load_dotenv()


URL = "https://openexchangerates.org/api/latest.json"
API_ID = os.getenv('API_ID')


def get_current_rate(request):

    # Проверка наличия курса в кеше
    cached_course = cache.get("cached_course")
    if cached_course:
        ten_latest_requests = cache.get("ten_latest_requests", [])
        return JsonResponse(
            {
                "attention": "Курс обновлялся ранее, прошло менее 10 секунд!",
                "ten_latest_requests": ten_latest_requests[::-1],
            }
        )

    # Запрашиваем курс с сайта
    url = "https://openexchangerates.org/api/latest.json"

    try:
        rate = currency_rate(URL, API_ID)
        СourseRequest.objects.create(
            request_date=datetime.now().date(), rate=rate
        )
        cache.set("cached_course", rate, timeout=10)
        ten_latest_requests = cache.get("ten_latest_requests", [])

        # Добавляем новый запрос с московским временем
        ten_latest_requests.append(
            {
                "request_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "rate": rate
            }
        )
        if len(ten_latest_requests) > 10:
            ten_latest_requests = ten_latest_requests[-10:]

        # Обновляем кеш с новыми данными
        cache.set("ten_latest_requests", ten_latest_requests, timeout=None)
        print(type(ten_latest_requests))
        # Возвращаем полученный курс и указываем источник данных
        return JsonResponse(
            {"ten_latest_requests": ten_latest_requests[::-1],}
        )
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)
