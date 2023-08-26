from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.SmallIntegerField('Категория')
    author = models.CharField('Автор', max_length=20)
    location = models.CharField('Локация товара', max_length=225)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advertisements'

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at == timezone.now().date():
            create_time = self.created_at.strftime('%H:%M.%S')
            return format_html('<span>Сегодня в {}</span>', create_time)
        date = self.created_at.strftime('%d.%m.%Y')
        time = self.created_at.strftime('%H:%M.%S')
        return format_html('<span>{} в {}</span>', date, time)
    
    @admin.display(description="Дата последних изменений")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at == timezone.now().date():
            updated_time = self.updated_at.strftime('%H:%M.%S')
            return format_html('<span>Сегодня в {}</span>', updated_time)
        date = self.updated_at.strftime('%d.%m.%Y')
        time = self.updated_at.strftime('%H:%M.%S')
        return format_html('<span>{} в {}</span>', date, time)