from django.shortcuts import render,redirect
from .models import History
import requests
from bs4 import BeautifulSoup as bs
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')


def search(request):
    if request.user.is_authenticated:
        if request.POST['search']:
            if request.method == 'POST':
                user = request.user
                search = request.POST['search']
                hs=History()
                hs.user=user
                hs.search = search
                hs.save()
                url = 'https://www.ask.com/web?q='+search
                res = requests.get(url)
                soup = bs(res.text, 'lxml')

                result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

                final_result = []

                for result in result_listings:
                    result_title = result.find(class_='PartialSearchResults-item-title').text
                    result_url = result.find('a').get('href')
                    result_desc = result.find(class_='PartialSearchResults-item-abstract').text

                    final_result.append((result_title, result_url, result_desc))

                context = {
                    'final_result': final_result
                }

                return render(request, 'search.html',context )

            else:
            
                return render(request, 'search.html' )
        else:
            return redirect("homepage")
    else:
        return redirect("login")


def histroy(request):
    # if request.user.is_authenticated:
    #     return render(requests,"history.html")
    # else:
    #     return redirect("login")
    his = History.objects.all().order_by("-id")
    return render(request, 'history.html',{'his':his} )