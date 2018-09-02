from django.db import models

class Emergency(models.Model):
    objects = models.Manager()
    contact = models.CharField(max_length=30, verbose_name='контакт')
    phone = models.CharField(max_length=50, verbose_name='телефон')
    def __str__(self):
        return self.contact
    class Meta:
        verbose_name='экстренный телефон'
        verbose_name_plural='экстренные телефоны'
        ordering=['contact']
