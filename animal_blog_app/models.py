from django.db import models

# Create your models here.


class Animal(models.Model):

    breed = models.CharField(max_length=50, verbose_name='Порода')
    nickname = models.CharField(max_length=50, verbose_name='Кличка')
    age = models.PositiveIntegerField(null=True, verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почта')
    price = models.PositiveIntegerField(default=1000, null=True, blank=True, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.breed} {self.nickname} {self.age}'

    def get_full_name(self):
        return f'{self.breed} {self.nickname}'

    def is_adult(self):
        return self.age >= 5

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'