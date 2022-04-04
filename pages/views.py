from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	context = {
		'name': 'Mwangi Morris Kinuthia',
		'school': 'Muranga University of Technology',
		'course': 'BSC Software Engineering',
		'admission': 2016,
	}
	# return HttpResponse("<h1>Hey Django</h1><b>This is home view</b>")
	return render(request, 'home.html', {})

def about_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hey Django</h1><b>This is about view</b>")
	return render(request, 'about.html', {})

def social_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hey Django</h1><b>This is social view</b>")
	return render(request, 'social.html', {})

def contact_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hey Django</h1><b>This is contact view</b>")
	return render(request, 'contact.html', {})