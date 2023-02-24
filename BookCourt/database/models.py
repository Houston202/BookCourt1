from django.db import models


class Books(models.Model):
    title = models.CharField('Название', max_length=250)
    date = models.IntegerField('Год')
    author = models.CharField('Автор', max_length=100)
    genre = models.CharField('Жанр', max_length=100)
    count_of_pages = models.IntegerField('Количество страниц')
    price = models.IntegerField('Цена')
    in_stock = models.IntegerField('В наличии')
    review = models.TextField('Описание', max_length=10000)

    def __str__(self):
        return self.title
