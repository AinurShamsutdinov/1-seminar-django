import datetime
import random

from django.db import models

# Create your models here.


class TossCoin(models.Model):
    result = models.CharField(max_length=100)
    date = models.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        rand = random.randrange(0, 2)
        if rand == 0:
            self.result = 'Head'
        else:
            self.result = 'Tail'
        self.date = datetime.datetime.now()

    def __str__(self):
        return f'Result: {self.result}, Date: {self.date}'


class Author(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Author: {self.name} {self.last_name} {self.email}'


class Article(models.Model):
    head = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'Article: {self.head} {self.content} {self.author}, published {self.published}'
    

class Commentary(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    date_creat = models.DateTimeField()
    date_edit = models.DateTimeField(null=True)


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    date_reg = models.DateTimeField()

    def __str__(self):
        return f'Client name: {self.name}, email: {self.email}'


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    amount = models.IntegerField()
    date_add = models.DateTimeField()

    def __str__(self):
        return f'Item name: {self.name}. Description: {self.description}. Price:{self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    full_price = models.FloatField()
    date_order = models.DateTimeField()

    def __str__(self):
        return f'{self.client} {self.items}'
    