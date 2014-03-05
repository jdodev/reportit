#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Country(models.Model):
	CountryID = models.AutoField(primary_key=True)
	Country = models.CharField(max_length=100, help_text='Country name', verbose_name=u'Country')

	def __unicode__(self):
		return self.Country

class Categories(models.Model):
	CategoryID = models.AutoField(primary_key=True)
	Category = models.CharField(max_length=100, help_text='Category name', verbose_name=u'Category')

	def __unicode__(self):
		return self.Category

class Report(models.Model):
	ReportID = models.AutoField(primary_key=True)
	Description = models.TextField(help_text='Report description', verbose_name=u'Description')
	Image = models.ImageField(upload_to='reports', help_text='Report image', verbose_name='Picture')
	Latitude = models.CharField(max_length=100, help_text='Latitude', verbose_name=u'Latitude')
	Longitude = models.CharField(max_length=100, help_text='Longitude', verbose_name=u'Longitude')
	User = models.ForeignKey(User)
	Date = models.DateTimeField(auto_now_add=True, help_text='Report date', verbose_name=u'Date')
	IdCountry = models.ForeignKey(Country)
	Anonymous = models.IntegerField(help_text='Anonymous?', verbose_name=u'Anonymous')
	Category = models.ForeignKey(Categories)

	def __unicode__(self):
		return self.User.User