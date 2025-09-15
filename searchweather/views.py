from django.shortcuts import render,redirect
from searchweather.models import SearchHistory
import os
# from django.contrib.auth.decorators import login_required
import requests
# @login_required(login_url='users/login')
def index(request):
    if request.method == "POST":
        city_user = request.POST.get('city','').title().strip()
        API_KEY = os.getenv('API_KEY') # Need your api key
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_user}&appid={API_KEY}&units=metric")
        if res.status_code == 200:
            data = res.json()
        else:
            return render(request,'searchweather/index.html',{'title':'Searching Weather'})
        weather = SearchHistory(user=request.user,city=city_user,temperature = data['main']['temp'],description = data['weather'][0]['description'])
        weather.save()
    else:
        return render(request,'searchweather/index.html',{'title':'Searching Weather'})
    context = {'weather':weather,'title':'Searching Weather'}
    return render(request,'searchweather/index.html',context)
def history(request):
    weather = SearchHistory.objects.filter(user=request.user).order_by('-search_date')
    return render(request,'searchweather/history.html',{'title':'History','weather':weather})