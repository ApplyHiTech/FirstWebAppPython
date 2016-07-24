from django.shortcuts import render, HttpResponse
import requests
import json
# Create your views here.

def index(request):
	return HttpResponse('Hello World!')

def test(request):
	return HttpResponse('This is a Test!')

def about(request):
	return render(request, 'app/about.html')

def profile(request):
	parsedData = []
	if request.method == 'POST': #The POST is the method
		username = request.POST.get('user') #Gets the value of user.
		req = requests.get('https://api.github.com/users/'+username)
		jsonList = []
		jsonList.append(json.loads(req.content))
		userData = {}
		for data in jsonList:
			userData['name']=data['name']
			userData['blog']=data['blog']
			userData['public_gists']=data['public_gists']
			userData['public_repos']=data['public_repos']
			userData['avatar_url']=data['avatar_url']
			userData['followers']=data['followers']
			userData['following']=data['following']
		parsedData.append(userData)

	return render(request, 'app/profile.html', {'data': parsedData})

def history(request):
	parsedData = []
	return render(request, 'app/history.html', {'data': parsedData})

