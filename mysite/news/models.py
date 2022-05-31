from distutils.command.upload import upload
from pyexpat import model
from tabnanny import verbose
from django.db import models

class News(models.Model):
    title = models.CharField("Заголовок", max_length=30)
    text = models.TextField("Текст статьи", max_length= 1500)
    image = models.ImageField("Изображение", upload_to="post/", blank=True)
    create = models.DateTimeField("Время создания", auto_now_add=True)
    blog = models.SlugField("Блог", max_length= 15)

    def __str__(self):
        return  self.title