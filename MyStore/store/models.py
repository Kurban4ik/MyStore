from django.db import models


class Stuff(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices=[('m', 'Male'), ('f', 'Female'), ('u', "Unisex")])
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=f'{str(name)[:30] + str(date)}')

    def __str__(self):
        return f'{self.name}, {self.price}'


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
