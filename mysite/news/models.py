from django.db import models

# class Post(models.Model):
#     title = models.CharField("Заголовок", max_length=50)
#     text = models.TextField("Текст статьи", max_length=1500)
#     image = models.ImageField("Изображение", upload_to="templates/news/image", blank=True)
#     create = models.DateTimeField("Создан", auto_now_add=True)

#     def __str__(self):
#         return self.title