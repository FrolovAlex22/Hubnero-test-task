from requests import get


def currency_rate(url: str, app_id: str):
    """Функция для запроса курса валюты с сайта"""
    request = f"{url}?app_id={app_id}&base=USD&symbols=RUB"
    response = get(request)
    if response.status_code == 200:
        data = response.json()
        return data.get("rates", {}).get("RUB")
    return None