from django.db import models

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