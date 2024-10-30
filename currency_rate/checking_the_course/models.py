from django.db import models


class СourseRequest(models.Model):
    """Модель запроса курса валюты."""
    request_date = models.DateTimeField(
        verbose_name='Дата и время запроса',
        auto_now_add=True,
        db_index=True,
    )
    rate = models.FloatField(
        verbose_name='Курс',
    )

    class Meta:
        ordering = ('-request_date',)
        verbose_name = 'Запрос курса валюты'
        verbose_name_plural = 'Список курсов валют'

    def __str__(self):
        return f'{self.request_date}: {self.rate}'
