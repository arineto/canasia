from django.db import models


class Country(models.Model):
	name = models.CharField(max_length=50)


class Sector(models.Model):
	name = models.CharField(max_length=100)


class Project(models.Model):
	country = models.ForeignKey('Country')
	sector = models.ForeignKey('Sector')
	company = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	picture = models.FileField(upload_to="pictures/")
	address = models.CharField(max_length=200)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
