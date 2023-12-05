from django.db import models

class Articles(models.Model):
    title=models.CharField('Название', max_length=75 )
    anons=models.CharField('Анонс', max_length= 250)
    full_text=models.TextField('Статья')
    date=models.DateTimeField('Дата публикации')
    img=models.ImageField(upload_to='files/events')

    def __str__(self):
        return self.title