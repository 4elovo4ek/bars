# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    #books = models.ManyToManyField(Book, blank=True, verbose_name="Книга")

    def __unicode__(self):
        return self.name

    class Meta():
        db_table = u'Автор'
        ordering = ["name"]



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta():
        db_table = u'Категория'

class Article(models.Model):
    class Meta():
        db_table = 'article'

    name = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, verbose_name="Автор")
    text = models.TextField()
    headshot = models.CharField(max_length=12)
    category = models.ForeignKey(Category, verbose_name='category', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_article = models.ForeignKey(Article)
