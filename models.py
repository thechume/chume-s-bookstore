# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    a_id = models.IntegerField(primary_key=True)
    a_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Books(models.Model):
    isbn = models.CharField(primary_key=True, max_length=30)
    title = models.CharField(max_length=35, blank=True, null=True)
    a = models.ForeignKey(Authors, models.DO_NOTHING, blank=True, null=True)
    cover = models.CharField(max_length=20183, blank=True, null=True)
    genre = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    avg_rating = models.FloatField(blank=True, null=True)
    format = models.CharField(max_length=20, blank=True, null=True)
    synopsis = models.CharField(max_length=4000, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Cart(models.Model):
    item_no = models.AutoField(primary_key=True)
    isbn = models.ForeignKey(Books, models.DO_NOTHING, db_column='isbn', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Discount(models.Model):
    isbn = models.ForeignKey(Books, models.DO_NOTHING, db_column='isbn', primary_key=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount'
