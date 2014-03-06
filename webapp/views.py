from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from django.core.files.uploadedfile import SimpleUploadedFile
import json

def getreports(request):
	qLat = request.GET.get('qLat', False)
	qLong = request.GET.get('qLong', False)

	qLatMax = float(qLat) + 0.4000000
	qLatMin = float(qLat) - 0.4000000

	qLongMax = float(qLong) + 0.4000000
	qLongMin = float(qLong) - 0.4000000

	resReports = Report.objects.extra(where=['Latitude <= ' + str(qLatMax) + ' AND Latitude >= '  + str(qLatMin) + ' AND Longitude <= ' + str(qLongMax) + ' AND Longitude >= ' + str(qLongMin)])[:50]

	lstReports = []

	for cReport in resReports:
		dctReports = {
		"ReportID":cReport.ReportID,
		"Description":cReport.Description,
		"Image":str(cReport.Image),
		"Latitude":cReport.Latitude,
		"Longitude":cReport.Longitude,
		"Date":cReport.Date,
		"Anonymous":cReport.Anonymous,
		"IdCategory":cReport.Category.CategoryID,
		"Category":cReport.Category.Category,
		"UserID":cReport.User.id,
		"UserFirstName":cReport.User.first_name,
		"UserLastName":cReport.User.last_name,
		"UserUserName":cReport.User.user,
		"IdCountry":cReport.IdCountry.CountryID,
		"Country":cReport.IdCountry.Country,
		}
		lstReports.append(dctReports)

	respuesta = {'success':True, 'message':'Success.', 'version':'v1', 'data':lstReports}
	return HttpResponse(json.dumps(respuesta), content_type='application/json')

def getcategories(request):
	resCategories = Categories.objects.all()

	lstCategories = []

	for cCategories in resCategories:
		dctCategories = {
		"CategoryID":cCategories.CategoryID,
		"Category":cCategories.Category,
		}
		lstCategories.append(dctCategories)

	respuesta = {'success':True, 'message':'Success.', 'version':'v1', 'data':lstCategories}
	return HttpResponse(json.dumps(respuesta), content_type='application/json')

def getcountries(request):
	resCountries = Country.objects.all()

	lstCountries = []

	for cCountry in resCountries:
		dctCountries = {
		"CountryID":cCountry.CountryID,
		"Country":cCountry.Country,
		}
		lstCountries.append(dctCountries)

	respuesta = {'success':True, 'message':'Success.', 'version':'v1', 'data':lstCountries}
	return HttpResponse(json.dumps(respuesta), content_type='application/json')





