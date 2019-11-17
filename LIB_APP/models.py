from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2,
                               error_messages={'max_length': 'Только 2 буквы!'})

    def __str__(self):
        return self.full_name


class Redaction(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            error_messages={'unique': 'Такая редакция уже существует!'})

    def __str__(self):
        return self.name


class BookHolder(models.Model):
    name = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    redaction = models.ForeignKey(Redaction,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True
                                  )
    reader = models.ForeignKey(BookHolder,
                               on_delete=models.SET_NULL,
                               default=None,
                               null=True,
                               blank=True
                               )

    def __str__(self):
        return f'{self.author.full_name} - {self.title}\n'
